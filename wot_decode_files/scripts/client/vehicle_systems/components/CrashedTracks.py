# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicle_systems/components/CrashedTracks.py
import weakref, math_utils, Math, BigWorld
from cgf_obsolete_script.auto_properties import AutoProperty
from cgf_obsolete_script.py_component import Component
from items.components.component_constants import MAIN_TRACK_PAIR_IDX
from items.vehicle_items import CHASSIS_ITEM_TYPE
from vehicle_systems import model_assembler
from vehicle_systems.tankStructure import getPartModelsFromDesc, TankPartNames, ModelsSetParams
from vehicle_systems.stricted_loading import loadingPriority, makeCallbackWeak
from constants import IS_EDITOR

class CrashedTrackController(Component):
    baseTracksComponent = AutoProperty()

    def __init__(self, vehicleDesc, trackFashion, modelsSet):
        self.__vehicleDesc = vehicleDesc
        self.__entity = None
        self.__modelsSet = modelsSet
        self.__baseTrackFashion = trackFashion
        self.baseTracksComponent = None
        if self.__vehicleDesc.chassis.tracks is not None:
            pairsCount = len(self.__vehicleDesc.chassis.tracks.trackPairs)
        else:
            pairsCount = 1
        self.__crashedTracks = {'left': [False] * pairsCount, 'right': [False] * pairsCount}
        self.__model = None
        self.__fashion = None
        self.__loading = False
        self.__isActive = False
        self.__visibilityMask = 15
        self.__debrisCrashedTracks = {'left': [False] * pairsCount, 'right': [False] * pairsCount}
        return

    def isLeftTrackBroken(self):
        for isTrackCrashed in self.__crashedTracks['left']:
            if isTrackCrashed:
                return True

        return False

    def isRightTrackBroken(self):
        for isTrackCrashed in self.__crashedTracks['right']:
            if isTrackCrashed:
                return True

        return False

    def setVehicle(self, entity):
        self.__entity = weakref.proxy(entity)

    def activate(self):
        if self.__entity is not None and self.__model is not None:
            self.__entity.addModel(self.__model)
            self.__applyVisibilityMask()
        self.__isActive = True
        return

    def deactivate(self):
        if self.__entity is not None and self.__model is not None:
            self.__entity.delModel(self.__model)
        self.__isActive = False
        self.__loading = False
        return

    def destroy(self):
        self.__reset()
        self.__entity = None
        self.__model = None
        self.__loading = False
        self.__baseTrackFashion = None
        self.__fashion = None
        self.baseTracksComponent = None
        return

    def setVisible(self, visibilityMask):
        self.__visibilityMask = visibilityMask
        self.__applyVisibilityMask()
        self.__setupTracksHiding()

    def addDebrisCrashedTrack(self, isLeft, pairIndex):
        side = 'left' if isLeft else 'right'
        self.__debrisCrashedTracks[side][pairIndex] = True

    def delDebrisCrashedTrack(self, isLeft, pairIndex):
        side = 'left' if isLeft else 'right'
        self.__debrisCrashedTracks[side][pairIndex] = False

    def __setupTrackAssembler(self, entity):
        modelNames = getPartModelsFromDesc(self.__vehicleDesc, ModelsSetParams(self.__modelsSet, 'destroyed', []))
        compoundAssembler = BigWorld.CompoundAssembler()
        compoundAssembler.addRootPart(modelNames.chassis, TankPartNames.CHASSIS, entity.filter.groundPlacingMatrix)
        compoundAssembler.name = TankPartNames.CHASSIS
        compoundAssembler.spaceID = entity.spaceID
        return compoundAssembler

    def __hasCrashedTracks(self):
        for side in self.__crashedTracks.values():
            for isTrackCrashed in side:
                if isTrackCrashed:
                    return True

        return False

    def addCrashedTrack(self, isLeft, pairIndex, isFlying=False):
        if self.__entity is None:
            return
        else:
            side = 'left' if isLeft else 'right'
            self.__crashedTracks[side][pairIndex] = True
            trackAssembler = self.__setupTrackAssembler(self.__entity)
            if self.__model is None and not isFlying:
                if not self.__loading:
                    self.__loadModel(trackAssembler)
            else:
                self.__setupTracksHiding()
            return

    def __loadModel(self, trackAssembler):
        if not IS_EDITOR:
            BigWorld.loadResourceListBG((
             trackAssembler,), makeCallbackWeak(self.__onModelLoaded), loadingPriority(self.__entity.id))
            self.__loading = True
        else:
            self.__loading = True
            resourceRefs = BigWorld.loadResourceListFG([trackAssembler])
            self.__onModelLoaded(resourceRefs)

    def delCrashedTrack(self, isLeft, pairIndex):
        side = 'left' if isLeft else 'right'
        self.__crashedTracks[side][pairIndex] = False
        hasCrashedTracks = self.__hasCrashedTracks()
        self.__loading = hasCrashedTracks and self.__loading
        if self.__entity is None:
            return
        else:
            if not hasCrashedTracks and self.__model is not None:
                if self.__model.isInWorld:
                    self.__entity.delModel(self.__model)
                self.__model = None
                self.__fashion = None
            self.__setupTracksHiding()
            return

    def receiveShotImpulse(self, direction, impulse):
        pass

    def __reset(self):
        if self.__entity is None:
            return
        else:
            if self.__vehicleDesc.chassis.tracks is not None:
                pairsCount = len(self.__vehicleDesc.chassis.tracks.trackPairs)
            else:
                pairsCount = 1
            self.__crashedTracks = {'left': [False] * pairsCount, 'right': [False] * pairsCount}
            self.__debrisCrashedTracks = {'left': [False] * pairsCount, 'right': [False] * pairsCount}
            if self.__model is not None:
                if self.__model.isInWorld:
                    self.__entity.delModel(self.__model)
                self.__model = None
                self.__fashion = None
                self.__baseTrackFashion = None
            return

    def __setupTracksHiding(self):
        force = self.__visibilityMask == 0
        trackIndices = []
        tracksPresent = self.__vehicleDesc.chassis.tracks is not None
        if self.__vehicleDesc.chassis.chassisType == CHASSIS_ITEM_TYPE.MONOLITHIC and tracksPresent:
            trackIndices = list(xrange(len(self.__vehicleDesc.chassis.tracks.trackPairs)))
        elif tracksPresent:
            trackIndices = [
             MAIN_TRACK_PAIR_IDX]
        if self.baseTracksComponent is not None and self.baseTracksComponent.valid:
            for i in trackIndices:
                hideLeftTrack = force or self.__crashedTracks['left'][i] or self.__debrisCrashedTracks['left'][i]
                hideRightTrack = force or self.__crashedTracks['right'][i] or self.__debrisCrashedTracks['right'][i]
                self.baseTracksComponent.disableTrack(hideLeftTrack, hideRightTrack, i)

        if self.__fashion is not None:
            for i in trackIndices:
                showLeftDestroyed = force or self.__crashedTracks['left'][i] and not self.__debrisCrashedTracks['left'][i]
                showRightDestroyed = force or self.__crashedTracks['right'][i] and not self.__debrisCrashedTracks['right'][i]
                self.__fashion.changeTrackVisibility(True, showLeftDestroyed, i)
                self.__fashion.changeTrackVisibility(False, showRightDestroyed, i)

        return

    def __applyVisibilityMask(self):
        colorPassEnabled = self.__visibilityMask & BigWorld.ColorPassBit != 0
        if self.__model is not None and self.__model.isValid and self.__model.isInWorld:
            self.__model.visible = self.__visibilityMask
            self.__model.skipColorPass = not colorPassEnabled
        return

    def __onModelLoaded(self, resources):
        if self.__entity is None or not self.__loading:
            return
        self.__loading = False
        model = resources[TankPartNames.CHASSIS]
        self.__model = model
        self.__model.matrix = self.__entity.filter.groundPlacingMatrix
        self.__fashion = BigWorld.WGVehicleFashion()
        matHandlers = self.__baseTrackFashion.getMaterialHandlers()
        for handler in matHandlers:
            self.__fashion.addMaterialHandler(handler)

        matHandlers = self.__baseTrackFashion.getTrackMaterialHandlers()
        for handler in matHandlers:
            self.__fashion.addTrackMaterialHandler(handler)

        model_assembler.setupTracksFashion(self.__vehicleDesc, self.__fashion)
        self.__model.setupFashions([self.__fashion])
        rotationMProv = math_utils.MatrixProviders.product(self.__entity.model.node('hull'), Math.MatrixInverse(self.__model.node('Tank')))
        self.__model.node('V', rotationMProv)
        self.__setupTracksHiding()
        if self.__isActive:
            self.__entity.addModel(self.__model)
            self.__applyVisibilityMask()
        return