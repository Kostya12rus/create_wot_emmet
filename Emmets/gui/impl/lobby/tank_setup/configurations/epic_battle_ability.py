# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/configurations/epic_battle_ability.py
from gui.impl.common.tabs_controller import tabUpdateFunc
from gui.impl.lobby.tank_setup.array_providers.frontline import BattleAbilityProvider
from gui.impl.lobby.tank_setup.configurations.base import BaseTankSetupTabsController, BaseDealPanel

class EpicBattleTabs(object):
    BATTLE_ABILITY = 'battleAbility'
    ALL = (
     BATTLE_ABILITY,)


class EpicBattleTabsController(BaseTankSetupTabsController):
    __slots__ = ()

    def getDefaultTab(self):
        return EpicBattleTabs.BATTLE_ABILITY

    @tabUpdateFunc(EpicBattleTabs.BATTLE_ABILITY)
    def _updateOptDevice(self, viewModel, isFirst=False):
        pass

    def tabOrderKey(self, tabName):
        return EpicBattleTabs.ALL.index(tabName)

    def _getAllProviders(self):
        return {EpicBattleTabs.BATTLE_ABILITY: BattleAbilityProvider}


class EpicBattleDealPanel(BaseDealPanel):

    @classmethod
    def updateDealPanelPrice(cls, vehicle, items, dealPanelModel):
        pass