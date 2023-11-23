# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/tooltips/battle_pass_points_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.reward_points_model import RewardPointsModel
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.vehicle_item_model import VehicleItemModel

class BattlePassPointsViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BattlePassPointsViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def rewardPoints(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardPointsType():
        return RewardPointsModel

    @property
    def vehiclesList(self):
        return self._getViewModel(1)

    @staticmethod
    def getVehiclesListType():
        return VehicleItemModel

    def _initialize(self):
        super(BattlePassPointsViewModel, self)._initialize()
        self._addViewModelProperty('rewardPoints', UserListModel())
        self._addViewModelProperty('vehiclesList', UserListModel())