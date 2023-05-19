# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/configurations/consumable.py
from gui.impl.common.tabs_controller import tabUpdateFunc
from gui.impl.lobby.tank_setup.configurations.base import BaseTankSetupTabsController
from gui.impl.lobby.tank_setup.array_providers.consumable import ConsumableDeviceProvider

class ConsumableTabs(object):
    DEFAULT = 'default'
    ALL = (
     DEFAULT,)


class ConsumableTabsController(BaseTankSetupTabsController):
    __slots__ = ()

    def getDefaultTab(self):
        return ConsumableTabs.DEFAULT

    @tabUpdateFunc(ConsumableTabs.DEFAULT)
    def _updateDefault(self, viewModel, isFirst=False):
        pass

    def tabOrderKey(self, tabName):
        return ConsumableTabs.ALL.index(tabName)

    def _getAllProviders(self):
        return {ConsumableTabs.DEFAULT: ConsumableDeviceProvider}