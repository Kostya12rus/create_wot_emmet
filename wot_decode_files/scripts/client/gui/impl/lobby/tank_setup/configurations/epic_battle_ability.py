# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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