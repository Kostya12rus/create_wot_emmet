# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/event/pre_queue/vehicles_watcher.py
from itertools import chain
from constants import Configs
from gui.prb_control.entities.base.pre_queue.vehicles_watcher import LimitedLevelVehiclesWatcher
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA
from helpers import dependency, server_settings
from skeletons.gui.game_control import IEventBattlesController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache

class EventBattleVehiclesWatcher(LimitedLevelVehiclesWatcher):
    __eventBattleCtrl = dependency.descriptor(IEventBattlesController)
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __itemsCache = dependency.descriptor(IItemsCache)

    def start(self):
        super(EventBattleVehiclesWatcher, self).start()
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChanged

    def stop(self):
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChanged
        super(EventBattleVehiclesWatcher, self).stop()

    def _getUnsuitableVehicles(self, onClear=False):
        vehs = self.__itemsCache.items.getVehicles(REQ_CRITERIA.INVENTORY | REQ_CRITERIA.VEHICLE.CLAN_WARS ^ REQ_CRITERIA.VEHICLE.BATTLE_ROYALE ^ REQ_CRITERIA.VEHICLE.EPIC_BATTLE).values()
        return chain.from_iterable((
         LimitedLevelVehiclesWatcher._getUnsuitableVehicles(self, onClear),
         vehs))

    def _getValidLevels(self):
        return self.__eventBattleCtrl.getModeSettings().levels

    @server_settings.serverSettingsChangeListener(Configs.EVENT_BATTLE.value)
    def __onServerSettingsChanged(self, diff):
        self._update()