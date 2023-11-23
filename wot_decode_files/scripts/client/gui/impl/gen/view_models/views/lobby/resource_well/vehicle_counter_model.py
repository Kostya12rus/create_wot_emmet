# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/resource_well/vehicle_counter_model.py
from frameworks.wulf import ViewModel

class VehicleCounterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(VehicleCounterModel, self).__init__(properties=properties, commands=commands)

    def getIsVehicleCountAvailable(self):
        return self._getBool(0)

    def setIsVehicleCountAvailable(self, value):
        self._setBool(0, value)

    def getVehicleCount(self):
        return self._getNumber(1)

    def setVehicleCount(self, value):
        self._setNumber(1, value)

    def getIsTopVehicle(self):
        return self._getBool(2)

    def setIsTopVehicle(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(VehicleCounterModel, self)._initialize()
        self._addBoolProperty('isVehicleCountAvailable', True)
        self._addNumberProperty('vehicleCount', 0)
        self._addBoolProperty('isTopVehicle', False)