# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/epic/pre_queue/vehicles_watcher.py
from itertools import chain
import typing
from gui.Scaleform.daapi.view.lobby.epicBattle.epic_helpers import isVehLevelUnlockableInBattle
from gui.prb_control.entities.base.pre_queue.vehicles_watcher import BaseVehiclesWatcher
from gui.shared.gui_items.Vehicle import Vehicle
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache

class EpicVehiclesWatcher(BaseVehiclesWatcher):
    _VEH_STATE_PRIORITIES = {Vehicle.VEHICLE_STATE.UNSUITABLE_TO_QUEUE: 1, 
       Vehicle.VEHICLE_STATE.WILL_BE_UNLOCKED_IN_BATTLE: 0}
    itemsCache = dependency.descriptor(IItemsCache)
    lobbyContext = dependency.descriptor(ILobbyContext)

    def _getUnsuitableVehicles(self, onClear=False):
        config = self.lobbyContext.getServerSettings().epicBattles
        vehs = self.itemsCache.items.getVehicles(REQ_CRITERIA.INVENTORY | ~REQ_CRITERIA.VEHICLE.LEVELS(config.validVehicleLevels)).itervalues()
        eventVehs = self.itemsCache.items.getVehicles(REQ_CRITERIA.INVENTORY | REQ_CRITERIA.VEHICLE.EVENT_BATTLE).itervalues()
        clanWarsVehs = self.itemsCache.items.getVehicles(REQ_CRITERIA.INVENTORY | REQ_CRITERIA.VEHICLE.CLAN_WARS).itervalues()
        comp7Vehs = self.itemsCache.items.getVehicles(REQ_CRITERIA.INVENTORY | REQ_CRITERIA.VEHICLE.COMP7).itervalues()
        return chain(vehs, eventVehs, clanWarsVehs, comp7Vehs)

    def _getVehiclesCustomStates(self, onClear=False):
        result = super(EpicVehiclesWatcher, self)._getVehiclesCustomStates(onClear)
        result.update({Vehicle.VEHICLE_STATE.WILL_BE_UNLOCKED_IN_BATTLE: self.__getWillBeUnlockedVehicles()})
        return result

    def __getWillBeUnlockedVehicles(self):
        vehicles = self.itemsCache.items.getVehicles(REQ_CRITERIA.INVENTORY | REQ_CRITERIA.CUSTOM((lambda v: isVehLevelUnlockableInBattle(v.level)))).itervalues()
        return vehicles