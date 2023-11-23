# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/winback/vehicle_bonus_model.py
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class VehicleBonusModel(ItemBonusModel):
    __slots__ = ()

    def __init__(self, properties=17, commands=0):
        super(VehicleBonusModel, self).__init__(properties=properties, commands=commands)

    def getIsElite(self):
        return self._getBool(9)

    def setIsElite(self, value):
        self._setBool(9, value)

    def getVehicleName(self):
        return self._getString(10)

    def setVehicleName(self, value):
        self._setString(10, value)

    def getUserName(self):
        return self._getString(11)

    def setUserName(self, value):
        self._setString(11, value)

    def getVehicleType(self):
        return self._getString(12)

    def setVehicleType(self, value):
        self._setString(12, value)

    def getNation(self):
        return self._getString(13)

    def setNation(self, value):
        self._setString(13, value)

    def getVehicleLvl(self):
        return self._getNumber(14)

    def setVehicleLvl(self, value):
        self._setNumber(14, value)

    def getPriceDiscount(self):
        return self._getNumber(15)

    def setPriceDiscount(self, value):
        self._setNumber(15, value)

    def getExpDiscount(self):
        return self._getNumber(16)

    def setExpDiscount(self, value):
        self._setNumber(16, value)

    def _initialize(self):
        super(VehicleBonusModel, self)._initialize()
        self._addBoolProperty('isElite', True)
        self._addStringProperty('vehicleName', '')
        self._addStringProperty('userName', '')
        self._addStringProperty('vehicleType', '')
        self._addStringProperty('nation', '')
        self._addNumberProperty('vehicleLvl', 0)
        self._addNumberProperty('priceDiscount', 0)
        self._addNumberProperty('expDiscount', 0)