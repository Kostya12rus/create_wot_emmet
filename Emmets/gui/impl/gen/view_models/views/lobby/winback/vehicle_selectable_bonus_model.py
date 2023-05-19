# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/winback/vehicle_selectable_bonus_model.py
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class VehicleSelectableBonusModel(ItemBonusModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(VehicleSelectableBonusModel, self).__init__(properties=properties, commands=commands)

    def getVehicleLvl(self):
        return self._getNumber(9)

    def setVehicleLvl(self, value):
        self._setNumber(9, value)

    def getPriceDiscount(self):
        return self._getNumber(10)

    def setPriceDiscount(self, value):
        self._setNumber(10, value)

    def getExpDiscount(self):
        return self._getNumber(11)

    def setExpDiscount(self, value):
        self._setNumber(11, value)

    def _initialize(self):
        super(VehicleSelectableBonusModel, self)._initialize()
        self._addNumberProperty('vehicleLvl', 0)
        self._addNumberProperty('priceDiscount', 0)
        self._addNumberProperty('expDiscount', 0)