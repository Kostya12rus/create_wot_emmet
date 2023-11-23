# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/tank_change_vehicle_model.py
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel

class TankChangeVehicleModel(VehicleModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(TankChangeVehicleModel, self).__init__(properties=properties, commands=commands)

    def getIsInInventory(self):
        return self._getBool(9)

    def setIsInInventory(self, value):
        self._setBool(9, value)

    def getIsElite(self):
        return self._getBool(10)

    def setIsElite(self, value):
        self._setBool(10, value)

    def getIsSelected(self):
        return self._getBool(11)

    def setIsSelected(self, value):
        self._setBool(11, value)

    def getIsTrainingAvailable(self):
        return self._getBool(12)

    def setIsTrainingAvailable(self, value):
        self._setBool(12, value)

    def _initialize(self):
        super(TankChangeVehicleModel, self)._initialize()
        self._addBoolProperty('isInInventory', False)
        self._addBoolProperty('isElite', False)
        self._addBoolProperty('isSelected', False)
        self._addBoolProperty('isTrainingAvailable', False)