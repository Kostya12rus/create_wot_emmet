# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/tooltips/vehicle_points_tooltip_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.reward_points_model import RewardPointsModel

class VehiclePointsTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(VehiclePointsTooltipViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def rewardPoints(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardPointsType():
        return RewardPointsModel

    def getVehicleLevel(self):
        return self._getNumber(1)

    def setVehicleLevel(self, value):
        self._setNumber(1, value)

    def getVehicleName(self):
        return self._getString(2)

    def setVehicleName(self, value):
        self._setString(2, value)

    def getVehicleType(self):
        return self._getString(3)

    def setVehicleType(self, value):
        self._setString(3, value)

    def getPointsCurrent(self):
        return self._getNumber(4)

    def setPointsCurrent(self, value):
        self._setNumber(4, value)

    def getPointsTotal(self):
        return self._getNumber(5)

    def setPointsTotal(self, value):
        self._setNumber(5, value)

    def getPointsReward(self):
        return self._getNumber(6)

    def setPointsReward(self, value):
        self._setNumber(6, value)

    def getIsSpecialVehicle(self):
        return self._getBool(7)

    def setIsSpecialVehicle(self, value):
        self._setBool(7, value)

    def getIsElite(self):
        return self._getBool(8)

    def setIsElite(self, value):
        self._setBool(8, value)

    def getBattleType(self):
        return self._getString(9)

    def setBattleType(self, value):
        self._setString(9, value)

    def _initialize(self):
        super(VehiclePointsTooltipViewModel, self)._initialize()
        self._addViewModelProperty('rewardPoints', UserListModel())
        self._addNumberProperty('vehicleLevel', 0)
        self._addStringProperty('vehicleName', '')
        self._addStringProperty('vehicleType', '')
        self._addNumberProperty('pointsCurrent', 0)
        self._addNumberProperty('pointsTotal', 0)
        self._addNumberProperty('pointsReward', 0)
        self._addBoolProperty('isSpecialVehicle', False)
        self._addBoolProperty('isElite', False)
        self._addStringProperty('battleType', '')