# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/configurations/halloween.py
from gui.impl.common.tabs_controller import tabUpdateFunc
from gui.impl.lobby.tank_setup.configurations.base import BaseTankSetupTabsController, BaseDealPanel
from gui.impl.lobby.tank_setup.array_providers.halloween import HalloweenConsumableProvider

class ConsumableTabs(object):
    DEFAULT = 'default'
    ALL = (
     DEFAULT,)


class HalloweenTabsController(BaseTankSetupTabsController):
    __slots__ = ()

    def getDefaultTab(self):
        return ConsumableTabs.DEFAULT

    @tabUpdateFunc(ConsumableTabs.DEFAULT)
    def _updateDefault(self, viewModel, isFirst=False):
        pass

    def tabOrderKey(self, tabName):
        return ConsumableTabs.ALL.index(tabName)

    def _getAllProviders(self):
        return {ConsumableTabs.DEFAULT: HalloweenConsumableProvider}


class HalloweenDealPanel(BaseDealPanel):

    @classmethod
    def addItem(cls, vehicle, item, prices):
        if item is None:
            return
        else:
            prices[cls._ON_VEHICLE_IN_SETUP] = False
            if item.isInInventory:
                prices[cls._IN_STORAGE] += 1
                return
            prices[cls._MONEY] += item.getBuyPrice().price
            return