# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle_royale/battle_results/player_vehicle_status_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.user_name_model import UserNameModel

class PlayerVehicleStatusModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PlayerVehicleStatusModel, self).__init__(properties=properties, commands=commands)

    @property
    def user(self):
        return self._getViewModel(0)

    @staticmethod
    def getUserType():
        return UserNameModel

    @property
    def killer(self):
        return self._getViewModel(1)

    @staticmethod
    def getKillerType():
        return UserNameModel

    def getReason(self):
        return self._getResource(2)

    def setReason(self, value):
        self._setResource(2, value)

    def _initialize(self):
        super(PlayerVehicleStatusModel, self)._initialize()
        self._addViewModelProperty('user', UserNameModel())
        self._addViewModelProperty('killer', UserNameModel())
        self._addResourceProperty('reason', R.invalid())