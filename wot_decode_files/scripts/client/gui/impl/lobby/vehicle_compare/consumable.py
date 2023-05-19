# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/vehicle_compare/consumable.py
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers
from gui.impl.lobby.tank_setup.array_providers.consumable import ConsumableDeviceProvider
from gui.impl.lobby.tank_setup.configurations.consumable import ConsumableTabsController, ConsumableTabs
from gui.impl.lobby.vehicle_compare.base_sub_view import CompareBaseSetupSubView

class CompareConsumableDeviceProvider(ConsumableDeviceProvider):

    def _fillStatus(self, model, item, slotID):
        super(CompareConsumableDeviceProvider, self)._fillStatus(model, item, slotID)
        if item.name in cmp_helpers.NOT_AFFECTED_EQUIPMENTS:
            model.setIsLocked(True)

    def _fillBuyPrice(self, *args, **kwargs):
        pass

    def _fillBuyStatus(self, model, item, isInstalledOrMounted):
        pass


class _CompareConsumableTabsController(ConsumableTabsController):

    def _getAllProviders(self):
        return {ConsumableTabs.DEFAULT: CompareConsumableDeviceProvider}


class CompareConsumableSetupSubView(CompareBaseSetupSubView):

    def _createTabsController(self):
        return _CompareConsumableTabsController()