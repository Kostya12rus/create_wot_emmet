# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/vehicle_bonus_model.py
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel

class VehicleBonusModel(RewardItemModel):
    __slots__ = ()

    def __init__(self, properties=19, commands=0):
        super(VehicleBonusModel, self).__init__(properties=properties, commands=commands)

    def getIsElite(self):
        return self._getBool(15)

    def setIsElite(self, value):
        self._setBool(15, value)

    def getVehicleName(self):
        return self._getString(16)

    def setVehicleName(self, value):
        self._setString(16, value)

    def getVehicleType(self):
        return self._getString(17)

    def setVehicleType(self, value):
        self._setString(17, value)

    def getVehicleLvl(self):
        return self._getNumber(18)

    def setVehicleLvl(self, value):
        self._setNumber(18, value)

    def _initialize(self):
        super(VehicleBonusModel, self)._initialize()
        self._addBoolProperty('isElite', True)
        self._addStringProperty('vehicleName', '')
        self._addStringProperty('vehicleType', '')
        self._addNumberProperty('vehicleLvl', 0)