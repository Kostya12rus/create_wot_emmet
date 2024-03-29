# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/comp7/pre_queue/vehicles_watcher.py
from itertools import chain
import typing
from constants import Configs
from gui.prb_control.entities.base.pre_queue.vehicles_watcher import LimitedLevelVehiclesWatcher, ForbiddenVehiclesWatcher
from gui.shared.gui_items.Vehicle import Vehicle
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency, server_settings
from skeletons.gui.game_control import IComp7Controller
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache

class Comp7VehiclesWatcher(LimitedLevelVehiclesWatcher, ForbiddenVehiclesWatcher):
    __comp7Ctrl = dependency.descriptor(IComp7Controller)
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __itemsCache = dependency.descriptor(IItemsCache)

    def start(self):
        super(Comp7VehiclesWatcher, self).start()
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChanged

    def stop(self):
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChanged
        super(Comp7VehiclesWatcher, self).stop()

    def _getUnsuitableVehicles(self, onClear=False):
        eventVehicles = self.__itemsCache.items.getVehicles(REQ_CRITERIA.INVENTORY | REQ_CRITERIA.VEHICLE.EVENT_BATTLE ^ REQ_CRITERIA.VEHICLE.CLAN_WARS).values()
        return chain.from_iterable((
         LimitedLevelVehiclesWatcher._getUnsuitableVehicles(self, onClear),
         ForbiddenVehiclesWatcher._getUnsuitableVehicles(self, onClear),
         eventVehicles))

    def _getForbiddenVehicleClasses(self):
        return self.__comp7Ctrl.getModeSettings().forbiddenClassTags

    def _getForbiddenVehicleTypes(self):
        return self.__comp7Ctrl.getModeSettings().forbiddenVehTypes

    def _getValidLevels(self):
        return self.__comp7Ctrl.getModeSettings().levels

    @server_settings.serverSettingsChangeListener(Configs.COMP7_CONFIG.value)
    def __onServerSettingsChanged(self, diff):
        self._update()