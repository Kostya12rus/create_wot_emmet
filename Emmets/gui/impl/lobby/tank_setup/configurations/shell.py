# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/configurations/shell.py
from gui.impl.common.tabs_controller import tabUpdateFunc
from gui.impl.lobby.tank_setup.array_providers.shell import ShellProvider
from gui.impl.lobby.tank_setup.configurations.base import BaseTankSetupTabsController, BaseDealPanel

class ShellTabs(object):
    SHELLS = 'shells'
    ALL = (
     SHELLS,)


class ShellTabsController(BaseTankSetupTabsController):
    __slots__ = ()

    def getDefaultTab(self):
        return ShellTabs.SHELLS

    @tabUpdateFunc(ShellTabs.SHELLS)
    def _updateDefault(self, viewModel, isFirst=False):
        pass

    def _getAllProviders(self):
        return {ShellTabs.SHELLS: ShellProvider}


class ShellDealPanel(BaseDealPanel):

    @classmethod
    def addItem(cls, vehicle, item, prices):
        inTankCount = 0
        intCD, _, currentCount = item
        for shell in vehicle.shells.setupLayouts:
            if shell.intCD == intCD:
                inTankCount = max(inTankCount, shell.count)

        if inTankCount >= currentCount:
            return
        inventoryItem = cls._itemsCache.items.getItemByCD(intCD)
        delta = currentCount - inTankCount
        storageDelta = min(delta, inventoryItem.inventoryCount)
        prices[cls._IN_STORAGE] += storageDelta
        delta -= storageDelta
        if delta:
            prices[cls._MONEY] += inventoryItem.getBuyPrice().price * delta