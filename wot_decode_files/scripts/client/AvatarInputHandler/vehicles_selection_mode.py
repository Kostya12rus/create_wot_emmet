# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/vehicles_selection_mode.py
import math, logging, weakref, BigWorld, Math, math_utils
from AvatarInputHandler import cameras, keys_handlers
from AvatarInputHandler.control_modes import IControlMode
from AvatarInputHandler.rotating_cursor_camera import RotatingCoursorCamera
from aih_constants import CTRL_MODE_NAME
from constants import ARENA_PERIOD, VEHICLE_SELECTION_BLOCK_DELAY
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.events import GameEvent
from helpers import dependency
from helpers.CallbackDelayer import CallbackDelayer
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache
from skeletons.gui.battle_session import IBattleSessionProvider
from vehicle_systems.tankStructure import TankPartIndexes
_logger = logging.getLogger(__name__)

class _CameraManager(object):
    CAMERA_TRANSITION_DURATION = 2
    __CAMERA_PITCH = math.radians(30)
    __MIN_CAMERA_DISTANCE = 10
    __CAM_CHANGING_SETTINGS = {'fov', 'windowSize'}
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)
    __settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, cfg):
        self.__initialCamSetup = None
        self.__camera = RotatingCoursorCamera(cfg)
        self.__cameraMover = _CameraMover(self.__camera)
        self.__pendingVehicles = set()
        return

    def start(self):
        self.__locateCameraOnAllVehicles()
        self.__settingsCore.onSettingsApplied += self.__onSettingsChanged

    def stop(self):
        self.__camera.destroy()
        self.__settingsCore.onSettingsApplied -= self.__onSettingsChanged
        if self.__pendingVehicles:
            self.__pendingVehicles = set()
            BigWorld.player().onVehicleEnterWorld -= self.__onVehicleEnteredWorld

    def reset(self):
        self.__locateCameraOnAllVehicles()

    def moveCameraToDefault(self):
        _, rotations, distance = self.__initialCamSetup
        self.__cameraMover.startMovementTo(rotations.yaw, rotations.pitch, distance, self.CAMERA_TRANSITION_DURATION)

    def handleMouseEvent(self, dx, dy, dz):
        self.__cameraMover.stop()
        self.__camera.handleMouseEvent(dx, dy, dz)

    def __onSettingsChanged(self, diff):
        if self.__CAM_CHANGING_SETTINGS.intersection(diff.keys()):
            self.__locateCameraOnAllVehicles()

    def __locateCameraOnAllVehicles(self):
        arenaDP = self.__sessionProvider.getArenaDP()
        yawSum = 0
        numVehs = 0
        vehiclesBBPoints = []
        targetPos = Math.Vector3()

        def _makeAdditionalPoints(basePoint, extraPoint):
            yield (
             extraPoint[0], basePoint[1], basePoint[2])
            yield (basePoint[0], extraPoint[1], basePoint[2])
            yield (basePoint[0], basePoint[1], extraPoint[2])

        for vehicleInfo in arenaDP.getVehiclesInfoIterator():
            if arenaDP.isAllyTeam(vehicleInfo.team):
                vehicleID = vehicleInfo.vehicleID
                if vehicleID in BigWorld.entities.keys():
                    vehicle = BigWorld.entities[vehicleID]
                else:
                    self.__pendingVehicles.add(vehicleID)
                    continue
                if vehicle.appearance.collisions is None:
                    continue
                vehMatrix = Math.Matrix(vehicle.matrix)
                targetPos += vehMatrix.translation
                hullBB = vehicle.appearance.collisions.getBoundingBox(TankPartIndexes.HULL)
                vehiclesBBPoints.extend([vehMatrix.applyPoint(hullBB[0]), vehMatrix.applyPoint(hullBB[1])])
                vehiclesBBPoints.extend(_makeAdditionalPoints(vehMatrix.applyPoint(hullBB[0]), vehMatrix.applyPoint(hullBB[1])))
                vehiclesBBPoints.extend(_makeAdditionalPoints(vehMatrix.applyPoint(hullBB[1]), vehMatrix.applyPoint(hullBB[0])))
                yawSum += vehMatrix.yaw + 2 * math.pi if vehMatrix.yaw < 0 else vehMatrix.yaw
                numVehs += 1

        if self.__pendingVehicles:
            _logger.info('Not all vehicles are in the world at the moment of camera setup. Skipped vehicles IDS: %s', self.__pendingVehicles)
            BigWorld.player().onVehicleEnterWorld += self.__onVehicleEnteredWorld
        if numVehs == 0:
            return
        else:
            averageYaw = yawSum / numVehs
            if averageYaw > math.pi:
                averageYaw -= 2 * math.pi
            targetPosition = targetPos.scale(1.0 / numVehs)
            yawMatrix = math_utils.createRTMatrix((averageYaw, self.__CAMERA_PITCH, 0), targetPosition)
            yawMatrix.invert()
            rotatedPoints = [ yawMatrix.applyPoint(p) for p in vehiclesBBPoints ]
            maxX = max(p.x for p in rotatedPoints)
            minX = min(p.x for p in rotatedPoints)
            maxZ = max(p.z for p in rotatedPoints)
            minZ = min(p.z for p in rotatedPoints)
            maxY = max(rp.y for rp in rotatedPoints if rp.x in (minX, maxX) or rp.z in (minZ, maxZ))
            width = maxX - minX
            height = maxZ - minZ
            hFov = BigWorld.projection().fov
            ratio = cameras.getScreenAspectRatio()
            halfFOVTan = math.tan(hFov / 2)
            distanceToTarget = max(width / (2 * halfFOVTan * ratio), height / (2 * halfFOVTan)) + maxY
            initialRotations = math_utils.createRotationMatrix((averageYaw, -self.__CAMERA_PITCH, 0))
            self.__initialCamSetup = (
             targetPosition, initialRotations, distanceToTarget)
            self.__setCamera()
            return

    def __setCamera(self):
        self.__camera.setup(*self.__initialCamSetup)

    def __onVehicleEnteredWorld(self, vehicle):
        if vehicle.id in self.__pendingVehicles:
            self.__pendingVehicles.remove(vehicle.id)
            if not self.__pendingVehicles:
                BigWorld.player().onVehicleEnterWorld -= self.__onVehicleEnteredWorld
                _logger.info('All vehicles have entered, repositioning the camera')
                self.__locateCameraOnAllVehicles()


class _CameraMover(CallbackDelayer):
    __TICK_DELAY = 0.01

    def __init__(self, camera):
        super(_CameraMover, self).__init__()
        self.__camera = camera
        self.__startParams, self.__finalParams, self.__totalChanges = {}, {}, {}
        self.__startTime, self.__endTime = (None, None)
        return

    def startMovementTo(self, finalYaw, finalPitch, pivotDistance, transtitionTime):
        self.stopCallback(self.__tick)
        camMatrix = Math.Matrix(self.__camera.sourceMatrix)
        self.__startParams['yaw'] = camMatrix.yaw
        self.__startParams['pitch'] = camMatrix.pitch
        self.__startParams['distance'] = self.__camera.pivotDistance
        self.__finalParams['yaw'] = finalYaw
        self.__finalParams['pitch'] = finalPitch
        self.__finalParams['distance'] = self.__camera.clampDistance(pivotDistance)
        self.__totalChanges['yaw'] = self.__getYawTotalChange(self.__startParams['yaw'], self.__finalParams['yaw'])
        self.__totalChanges['pitch'] = self.__finalParams['pitch'] - self.__startParams['pitch']
        self.__totalChanges['distance'] = self.__finalParams['distance'] - self.__startParams['distance']
        self.__startTime = BigWorld.time()
        self.__endTime = self.__startTime + transtitionTime
        self.delayCallback(self.__TICK_DELAY, self.__tick)

    def stop(self):
        self.stopCallback(self.__tick)

    def __tick(self):
        currTime = BigWorld.time()
        timePassed = currTime - self.__startTime
        totalTime = self.__endTime - self.__startTime
        newYaw = self.__getNewValueForParameter('yaw', timePassed, totalTime)
        newPitch = self.__getNewValueForParameter('pitch', timePassed, totalTime)
        newDistance = self.__getNewValueForParameter('distance', timePassed, totalTime)
        self.__camera.move(math_utils.createRotationMatrix((newYaw, newPitch, 0)), newDistance)
        if currTime < self.__endTime:
            self.delayCallback(self.__TICK_DELAY, self.__tick)

    def __getYawTotalChange(self, startYaw, finalYaw):
        adjustedStartYaw = startYaw if startYaw > 0 else math.pi + (math.pi - abs(startYaw))
        adjustedFinalYaw = finalYaw if finalYaw > 0 else math.pi + (math.pi - abs(finalYaw))
        adjustedDiff = adjustedFinalYaw - adjustedStartYaw
        if adjustedDiff == 0:
            return 0
        return min(adjustedDiff, math.copysign(1, -1 * adjustedDiff) * (2 * math.pi - abs(adjustedDiff)), key=abs)

    def __getNewValueForParameter(self, paramName, timePassed, totalTime):
        totalChange = self.__totalChanges[paramName]
        if timePassed > totalTime or totalChange == 0:
            return self.__finalParams[paramName]
        return self.__startParams[paramName] + math_utils.easeInOutCubic(timePassed, totalChange, totalTime)


class VehiclesSelectionControlMode(IControlMode):
    __dynamicObjectsCache = dependency.descriptor(IBattleDynamicObjectsCache)
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, config, avatarInputHandler):
        self.__aih = weakref.proxy(avatarInputHandler)
        self.__camManager = _CameraManager(config['camera'])
        self.__arenaPeriod = None
        self.__ownVehicleEffectGO = None
        self.__lockedState = False
        self.__lockStartTime = 0
        self.__callbackDelayer = CallbackDelayer()
        return

    def destroy(self):
        if self.__camManager is not None:
            self.__camManager.stop()
        self.__camManager = None
        self.__callbackDelayer.destroy()
        self.__callbackDelayer = None
        return

    def enable(self, **args):
        self.__camManager.start()
        arena = BigWorld.player().arena
        arena.onPeriodChange += self.__onArenaPeriodChanged
        self.__updateArenaPeriod(arena.period, arena.periodEndTime)

    def disable(self):
        arena = BigWorld.player().arena
        arena.onPeriodChange -= self.__onArenaPeriodChanged
        self.__callbackDelayer.clearCallbacks()

    def alwaysReceiveKeyEvents(self, isDown=True):
        return isDown

    def handleKeyEvent(self, isDown, key, mods, event=None):
        prbCtrl = self.__guiSessionProvider.dynamic.comp7PrebattleSetup
        if (prbCtrl is None or prbCtrl.isSelectionConfirmed()) and keys_handlers.processAmmoSelection(key):
            return True
        else:
            return

    def handleMouseEvent(self, dx, dy, dz):
        if self.__lockedState:
            return False
        self.__camManager.handleMouseEvent(dx, dy, math_utils.clamp(-1, 1, dz))
        return True

    def onRecreateDevice(self):
        self.__camManager.reset()

    def moveCameraToDefault(self):
        lockIsSoon = 0 < self.__lockStartTime < BigWorld.serverTime() + self.__camManager.CAMERA_TRANSITION_DURATION
        if not self.__lockedState and not lockIsSoon:
            self.__camManager.moveCameraToDefault()

    def __onLockedState(self):
        self.__lockedState = True
        g_eventBus.handleEvent(GameEvent(GameEvent.PREBATTLE_INPUT_STATE_LOCKED), scope=EVENT_BUS_SCOPE.BATTLE)
        self.__aih.ctrls[CTRL_MODE_NAME.ARCADE].camera.enable(camTransitionParams={'cameraTransitionDuration': self.__camManager.CAMERA_TRANSITION_DURATION})

    def __onArenaPeriodChanged(self, period, periodEndTime, *_):
        self.__updateArenaPeriod(period, periodEndTime)

    def __updateArenaPeriod(self, period, periodEndTime):
        if period == ARENA_PERIOD.BATTLE:
            self.__aih.onControlModeChanged(CTRL_MODE_NAME.ARCADE)
        elif period == ARENA_PERIOD.PREBATTLE:
            self.__lockStartTime = periodEndTime - VEHICLE_SELECTION_BLOCK_DELAY
            timeTillEnd = periodEndTime - BigWorld.serverTime()
            self.__callbackDelayer.delayCallback(timeTillEnd - VEHICLE_SELECTION_BLOCK_DELAY, self.__onLockedState)
        self.__arenaPeriod = period