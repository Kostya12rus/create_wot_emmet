# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/tooltips/reward_points_model.py
from frameworks.wulf import ViewModel

class RewardPointsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(RewardPointsModel, self).__init__(properties=properties, commands=commands)

    def getTopCount(self):
        return self._getNumber(0)

    def setTopCount(self, value):
        self._setNumber(0, value)

    def getPointsWin(self):
        return self._getNumber(1)

    def setPointsWin(self, value):
        self._setNumber(1, value)

    def getPointsLose(self):
        return self._getNumber(2)

    def setPointsLose(self, value):
        self._setNumber(2, value)

    def getIsSpecial(self):
        return self._getBool(3)

    def setIsSpecial(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(RewardPointsModel, self)._initialize()
        self._addNumberProperty('topCount', 0)
        self._addNumberProperty('pointsWin', 0)
        self._addNumberProperty('pointsLose', 0)
        self._addBoolProperty('isSpecial', False)