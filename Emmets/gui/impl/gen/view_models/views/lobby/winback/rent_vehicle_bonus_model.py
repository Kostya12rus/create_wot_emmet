# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/winback/rent_vehicle_bonus_model.py
from enum import Enum
from gui.impl.gen.view_models.views.lobby.winback.vehicle_bonus_model import VehicleBonusModel

class RentType(Enum):
    TIME = 'time'
    WINS = 'wins'
    BATTLES = 'battles'


class RentVehicleBonusModel(VehicleBonusModel):
    __slots__ = ()

    def __init__(self, properties=19, commands=0):
        super(RentVehicleBonusModel, self).__init__(properties=properties, commands=commands)

    def getRentType(self):
        return RentType(self._getString(17))

    def setRentType(self, value):
        self._setString(17, value.value)

    def getRentDuration(self):
        return self._getNumber(18)

    def setRentDuration(self, value):
        self._setNumber(18, value)

    def _initialize(self):
        super(RentVehicleBonusModel, self)._initialize()
        self._addStringProperty('rentType')
        self._addNumberProperty('rentDuration', 0)