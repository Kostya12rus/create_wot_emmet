# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/battle_pass_points_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel

class BattlePassPointsViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BattlePassPointsViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def pointsTops(self):
        return self._getViewModel(0)

    @staticmethod
    def getPointsTopsType():
        return UserListModel

    @property
    def vehiclesList(self):
        return self._getViewModel(1)

    @staticmethod
    def getVehiclesListType():
        return UserListModel

    def _initialize(self):
        super(BattlePassPointsViewModel, self)._initialize()
        self._addViewModelProperty('pointsTops', UserListModel())
        self._addViewModelProperty('vehiclesList', UserListModel())