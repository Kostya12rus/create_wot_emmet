# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_royale/battle_result_view/user_battle_info_model.py
from gui.impl.gen.view_models.common.user_name_model import UserNameModel

class UserBattleInfoModel(UserNameModel):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(UserBattleInfoModel, self).__init__(properties=properties, commands=commands)

    def getVehicleName(self):
        return self._getString(10)

    def setVehicleName(self, value):
        self._setString(10, value)

    def getVehicleType(self):
        return self._getString(11)

    def setVehicleType(self, value):
        self._setString(11, value)

    def getVehicleLevel(self):
        return self._getNumber(12)

    def setVehicleLevel(self, value):
        self._setNumber(12, value)

    def getDamage(self):
        return self._getNumber(13)

    def setDamage(self, value):
        self._setNumber(13, value)

    def getKills(self):
        return self._getNumber(14)

    def setKills(self, value):
        self._setNumber(14, value)

    def _initialize(self):
        super(UserBattleInfoModel, self)._initialize()
        self._addStringProperty('vehicleName', '')
        self._addStringProperty('vehicleType', '')
        self._addNumberProperty('vehicleLevel', 1)
        self._addNumberProperty('damage', 0)
        self._addNumberProperty('kills', 0)