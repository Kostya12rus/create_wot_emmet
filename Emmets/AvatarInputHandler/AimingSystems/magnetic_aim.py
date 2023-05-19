# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/AimingSystems/magnetic_aim.py
from collections import namedtuple
from itertools import chain
import math, BigWorld
from Math import Vector3, Matrix
import math_utils

class MagneticAimSettings(object):
    MAGNETIC_ANGLE = 2.25
    KEY_DELAY_SEC = 0.5

    @staticmethod
    def getMagneticAngle():
        return math.cos(math.radians(MagneticAimSettings.MAGNETIC_ANGLE))


_TargetVeh = namedtuple('TargetVehicle', ('vehicleRef', 'dotResult', 'distance'))

def magneticAimProcessor(previousSimpleTarget=None, previousMagneticTarget=None):
    if BigWorld.target() is None:
        target = magneticAimFindTarget()
        if target and target != previousSimpleTarget and target != previousMagneticTarget:
            BigWorld.player().autoAim(target=target, magnetic=True)
            return target
    return previousSimpleTarget


def magneticAimFindTarget():
    vehicleAttached = BigWorld.player().getVehicleAttached()
    aimCamera = BigWorld.player().inputHandler.ctrl.camera
    aimCameraDirection = aimCamera.aimingSystem.matrixProvider.applyToAxis(2)
    if vehicleAttached is None or not vehicleAttached.isAlive():
        return
    minAngleVehicle = None
    for vehicleID in BigWorld.player().arena.vehicles.iterkeys():
        vehicle = BigWorld.entity(vehicleID)
        if vehicle is None:
            continue
        allyOrSelfVehicle = vehicle.publicInfo['team'] == BigWorld.player().team or vehicle.isPlayerVehicle
        if allyOrSelfVehicle or not vehicle.isStarted or not vehicle.isAlive():
            continue
        vehiclePositionDirection = vehicle.position - aimCamera.camera.position
        vehiclePositionDirection.normalise()
        dotResult = vehiclePositionDirection.dot(aimCameraDirection)
        targetDistance = vehicle.position - vehicleAttached.position
        if dotResult < MagneticAimSettings.getMagneticAngle():
            continue
        if not isVehicleVisibleFromCamera(vehicle, aimCamera):
            continue
        veh = _TargetVeh(vehicleRef=vehicle, dotResult=dotResult, distance=targetDistance.length)
        if minAngleVehicle is None or dotResult >= minAngleVehicle.dotResult:
            minAngleVehicle = veh
        if minAngleVehicle is not None and math_utils.almostZero(dotResult - minAngleVehicle.dotResult):
            if targetDistance.length < minAngleVehicle.distance:
                minAngleVehicle = veh

    pickedVehicle = None
    if minAngleVehicle:
        pickedVehicle = minAngleVehicle.vehicleRef
    return pickedVehicle


def getVehiclePointsGen(vehicle):
    vehicleDesr = vehicle.typeDescriptor
    hullPos = vehicleDesr.chassis.hullPosition
    hullBboxMin, hullBboxMax, _ = vehicleDesr.hull.hitTester.bbox
    turretPosOnHull = vehicleDesr.hull.turretPositions[0]
    turretLocalTopY = max(hullBboxMax.y, turretPosOnHull.y + vehicleDesr.turret.hitTester.bbox[1].y)
    yield Vector3(0.0, hullPos.y + turretLocalTopY, 0.0)
    gunPosOnHull = turretPosOnHull + vehicleDesr.turret.gunPosition
    yield hullPos + gunPosOnHull
    hullLocalCenterY = (hullBboxMin.y + hullBboxMax.y) / 2.0
    hullLocalPt1 = Vector3(0.0, hullLocalCenterY, hullBboxMax.z)
    yield hullPos + hullLocalPt1
    hullLocalPt2 = Vector3(0.0, hullLocalCenterY, hullBboxMin.z)
    yield hullPos + hullLocalPt2
    hullLocalCenterZ = (hullBboxMin.z + hullBboxMax.z) / 2.0
    hullLocalPt3 = Vector3(hullBboxMax.x, gunPosOnHull.y, hullLocalCenterZ)
    yield hullPos + hullLocalPt3
    hullLocalPt4 = Vector3(hullBboxMin.x, gunPosOnHull.y, hullLocalCenterZ)
    yield hullPos + hullLocalPt4


def getVisibilityCheckPointsGen(vehicle):
    matrix = Matrix(vehicle.matrix)
    return chain((vehicle.position,), (matrix.applyPoint(pt) for pt in getVehiclePointsGen(vehicle)))


def isVehicleVisibleFromCamera(vehicle, aimCamera):
    for vehiclePoint in getVisibilityCheckPointsGen(vehicle):
        startPos = aimCamera.camera.position
        endPos = vehiclePoint
        testResStatic = BigWorld.wg_collideSegment(BigWorld.player().spaceID, startPos, endPos, 128)
        if testResStatic is None:
            testResDynamic = BigWorld.wg_collideDynamic(BigWorld.player().spaceID, startPos, endPos, BigWorld.player().playerVehicleID)
            if testResDynamic is None:
                return True

    return False