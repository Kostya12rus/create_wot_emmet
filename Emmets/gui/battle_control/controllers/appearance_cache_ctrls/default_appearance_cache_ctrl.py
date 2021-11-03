# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/appearance_cache_ctrls/default_appearance_cache_ctrl.py
import logging, BigWorld
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from skeletons.vehicle_appearance_cache import IAppearanceCache
from helpers import dependency
from soft_exception import SoftException
from vehicle_systems.appearance_cache import VehicleAppearanceCacheInfo
_logger = logging.getLogger(__name__)

class DefaultAppearanceCacheController(IArenaVehiclesController):
    _appearanceCache = dependency.descriptor(IAppearanceCache)

    def __init__(self, setup):
        super(DefaultAppearanceCacheController, self).__init__()
        self._arena = None
        self._spaceLoaded = False
        self._precacheFunc = None
        return

    def getControllerID(self):
        return BATTLE_CTRL_ID.APPEARANCE_CACHE_CTRL

    def startControl(self, battleCtx, arenaVisitor):
        self._arena = BigWorld.player().arena
        self._setCacheAppearanceFunc()
        if self._precacheFunc is None:
            raise SoftException('DefaultAppearanceCacheController _precacheFunc can not be None')
        return

    def stopControl(self):
        self._removeListeners()
        self._appearanceCache.clear()
        self._spaceLoaded = False
        self._arena = None
        self._precacheFunc = None
        return

    def arenaLoadCompleted(self):
        self._addListeners()
        self._spaceLoaded = True
        self._precache(self._arena.vehicles)

    def addVehicleInfo(self, vo, arenaDP):
        vInfo = self._arena.vehicles[vo.vehicleID]
        self._precache({vo.vehicleID: vInfo})

    def updateVehiclesInfo(self, updated, arenaDP):
        for _, vo in updated:
            self.addVehicleInfo(vo, arenaDP)

    def _addListeners(self):
        if hasattr(self._arena.componentSystem, 'playerDataComponent'):
            self._arena.componentSystem.playerDataComponent.onPlayerGroupsUpdated += self._onPlayerGroupsUpdated

    def _removeListeners(self):
        if self._spaceLoaded and hasattr(self._arena.componentSystem, 'playerDataComponent'):
            self._arena.componentSystem.playerDataComponent.onPlayerGroupsUpdated -= self._onPlayerGroupsUpdated

    def _setCacheAppearanceFunc(self):
        if self._arena.arenaType.numPlayerGroups > 0 and hasattr(self._arena.componentSystem, 'playerDataComponent'):
            self._precacheFunc = self._cachePlayerGroupVehicles
        else:
            self._precacheFunc = self._cacheAllVehicles

    def _precache(self, vehiclesInfo, groupIDs=None):
        if not self._spaceLoaded:
            return
        self._precacheFunc(vehiclesInfo, groupIDs)

    def _cacheAllVehicles(self, vehiclesInfo, _=None):
        for vId, vInfo in vehiclesInfo.iteritems():
            self.__cacheVehicle(vId, vInfo)

    def _cachePlayerGroupVehicles(self, vehiclesInfo, groupIDs=None):
        playerGroupId = self._arena.componentSystem.playerDataComponent.getPlayerGroupForPlayer()
        for vId, vInfo in vehiclesInfo.iteritems():
            if groupIDs is not None:
                groupId = groupIDs[vId]
            else:
                groupId = self._arena.componentSystem.playerDataComponent.getPlayerGroupForVehicle(vId)
            if groupId != playerGroupId:
                continue
            self.__cacheVehicle(vId, vInfo)

        return

    def invalidateVehiclesInfo(self, arenaDP):
        self._precache(self._arena.vehicles)

    def _onPlayerGroupsUpdated(self, vIds):
        if not self._arena.vehicles:
            return
        else:
            playerVehicleId = getattr(BigWorld.player(), 'playerVehicleID', 0)
            if playerVehicleId <= 0:
                return
            groupIDs = None
            if playerVehicleId in vIds:
                vehicleInfos = self._arena.vehicles
            else:
                vehicleInfos = {vId:self._arena.vehicles[vId] for vId in vIds}
                groupIDs = vIds
            self._precache(vehicleInfos, groupIDs)
            return

    def __cacheVehicle(self, vId, vInfo):
        typeDescriptor = vInfo['vehicleType']
        if typeDescriptor is not None:
            isAlive = vInfo['isAlive']
            outfitCD = vInfo['outfitCD']
            info = VehicleAppearanceCacheInfo(typeDescr=typeDescriptor, health=int(isAlive), isCrewActive=isAlive, isTurretDetached=False, outfitCD=outfitCD)
            self._appearanceCache.getAppearance(vId, info)
        return