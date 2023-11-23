# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/array_providers/halloween.py
from gui.impl.gen.view_models.constants.item_highlight_types import ItemHighlightTypes
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.hw_consumable_slot_model import HwConsumableSlotModel
from gui.impl.lobby.tank_setup.array_providers.base import VehicleBaseArrayProvider
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA

class HalloweenConsumableProvider(VehicleBaseArrayProvider):
    __slots__ = ()

    def getItemViewModel(self):
        return HwConsumableSlotModel()

    def createSlot(self, item, ctx):
        model = super(HalloweenConsumableProvider, self).createSlot(item, ctx)
        model.setImageName(item.descriptor.iconName)
        model.setItemName(item.name)
        model.setDescription(item.shortDescription)
        model.setIsBuiltIn(False)
        isEnough = item.mayPurchaseWithExchange(self._itemsCache.items.stats.money, self._itemsCache.items.shop.exchangeRate)
        model.setIsBuyMoreDisabled(not isEnough)
        self._fillHighlights(model, item)
        self._fillBuyPrice(model, item)
        return model

    def updateSlot(self, model, item, ctx):
        super(HalloweenConsumableProvider, self).updateSlot(model, item, ctx)
        isInstalledOrMounted = item in self._getCurrentLayout() or item in self._getInstalledLayout()
        self._fillStatus(model, item, ctx.slotID)
        self._fillBuyStatus(model, item, isInstalledOrMounted)

    def _fillHighlights(self, model, item):
        if item.isBuiltIn:
            model.setOverlayType(ItemHighlightTypes.BUILT_IN_EQUIPMENT)
            model.setHighlightType(ItemHighlightTypes.BUILT_IN_EQUIPMENT)

    def _mayInstall(self, item, slotID=None):
        vehicle = self._getVehicle()
        installed = vehicle.hwConsumables.installed
        layout = vehicle.hwConsumables.layout
        vehicle.hwConsumables.installed = layout
        isFit, reason = item.mayInstall(vehicle, slotID)
        vehicle.hwConsumables.installed = installed
        installedItem = layout[slotID]
        if installedItem is not None and installedItem.isBuiltIn and item not in layout:
            return (False, '')
        else:
            return (
             isFit, reason)

    @classmethod
    def _getItemTypeID(cls):
        return (GUI_ITEM_TYPE.EQUIPMENT,)

    def _getItemCriteria(self):
        return REQ_CRITERIA.VEHICLE.HAS_TAGS(['halloween_equipment']) | ~REQ_CRITERIA.VEHICLE.HAS_TAGS(['empty_slot'])

    def _getEquipment(self):
        return self._getVehicle().consumables