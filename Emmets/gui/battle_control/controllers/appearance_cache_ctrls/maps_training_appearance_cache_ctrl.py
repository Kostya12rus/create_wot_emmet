# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/appearance_cache_ctrls/maps_training_appearance_cache_ctrl.py
import logging, BigWorld
from helpers import uniprof
from items.vehicles import VehicleDescriptor
from gui.battle_control.controllers.appearance_cache_ctrls.event_appearance_cache_ctrl import EventAppearanceCacheController
from vehicle_outfit.outfit import Outfit
from vehicle_systems import model_assembler
from vehicle_systems.camouflages import getOutfitComponent
from vehicle_systems.tankStructure import ModelsSetParams, ModelStates
_logger = logging.getLogger(__name__)

class MapsTrainingAppearanceCacheController(EventAppearanceCacheController):

    @uniprof.regionDecorator(label='MapsTrainingAppearanceCacheController.updateSpawnList', scope='wrap')
    def updateSpawnList(self, spawnListData):
        toAdd = spawnListData.difference(self._spawnList)
        toRemove = self._spawnList.difference(spawnListData)
        for data in toAdd:
            vDesc = VehicleDescriptor(compactDescr=data.vehicleCD)
            prereqs = set(vDesc.prerequisites())
            outfit = Outfit(component=getOutfitComponent(data.outfitCD), vehicleCD=data.vehicleCD)
            modelsSetParams = ModelsSetParams(outfit.modelsSet, ModelStates.UNDAMAGED, [])
            compoundAssembler = model_assembler.prepareCompoundAssembler(vDesc, modelsSetParams, BigWorld.camera().spaceID)
            prereqs.add(compoundAssembler)
            self._appearanceCache.loadResources(data.vehicleCD, list(prereqs))

        for data in toRemove:
            self._appearanceCache.unloadResources(data.vehicleCD)

        self._spawnList = spawnListData
        _logger.debug('MapsTrainingAppearanceCacheController SpawnList cache updated=%s', spawnListData)