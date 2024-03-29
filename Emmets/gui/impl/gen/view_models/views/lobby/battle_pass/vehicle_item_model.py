# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/vehicle_item_model.py
from frameworks.wulf import ViewModel

class VehicleItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(VehicleItemModel, self).__init__(properties=properties, commands=commands)

    def getVehicleType(self):
        return self._getString(0)

    def setVehicleType(self, value):
        self._setString(0, value)

    def getVehicleLevel(self):
        return self._getNumber(1)

    def setVehicleLevel(self, value):
        self._setNumber(1, value)

    def getVehicleName(self):
        return self._getString(2)

    def setVehicleName(self, value):
        self._setString(2, value)

    def getVehicleBonus(self):
        return self._getNumber(3)

    def setVehicleBonus(self, value):
        self._setNumber(3, value)

    def getVehicleTop(self):
        return self._getNumber(4)

    def setVehicleTop(self, value):
        self._setNumber(4, value)

    def getTextResourceID(self):
        return self._getNumber(5)

    def setTextResourceID(self, value):
        self._setNumber(5, value)

    def _initialize(self):
        super(VehicleItemModel, self)._initialize()
        self._addStringProperty('vehicleType', '')
        self._addNumberProperty('vehicleLevel', 0)
        self._addStringProperty('vehicleName', '')
        self._addNumberProperty('vehicleBonus', 0)
        self._addNumberProperty('vehicleTop', 0)
        self._addNumberProperty('textResourceID', 0)