# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/configurations/battle_booster.py
from gui.impl.common.tabs_controller import tabUpdateFunc
from gui.impl.lobby.tank_setup.array_providers.battle_booster import OptDeviceBattleBoosterProvider, CrewBattleBoosterProvider
from gui.impl.lobby.tank_setup.configurations.base import BaseTankSetupTabsController

class BattleBoosterTabs(object):
    OPT_DEVICE = 'optDevice'
    CREW = 'crew'
    ALL = (
     OPT_DEVICE, CREW)


class BattleBoostersTabsController(BaseTankSetupTabsController):
    __slots__ = ()

    def getDefaultTab(self):
        return BattleBoosterTabs.OPT_DEVICE

    @tabUpdateFunc(BattleBoosterTabs.OPT_DEVICE)
    def _updateOptDevice(self, viewModel, isFirst=False):
        pass

    @tabUpdateFunc(BattleBoosterTabs.CREW)
    def _updateCrew(self, viewModel, isFirst=False):
        pass

    def tabOrderKey(self, tabName):
        return BattleBoosterTabs.ALL.index(tabName)

    def _getAllProviders(self):
        return {BattleBoosterTabs.OPT_DEVICE: OptDeviceBattleBoosterProvider, 
           BattleBoosterTabs.CREW: CrewBattleBoosterProvider}