# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/ranked/ranked_qualification_rewards_view_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.ranked.ranked_qualification_rewards_battle_bonus_model import RankedQualificationRewardsBattleBonusModel

class RankedQualificationRewardsViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(RankedQualificationRewardsViewModel, self).__init__(properties=properties, commands=commands)

    def getCurrentProgress(self):
        return self._getNumber(0)

    def setCurrentProgress(self, value):
        self._setNumber(0, value)

    def getTotalProgress(self):
        return self._getNumber(1)

    def setTotalProgress(self, value):
        self._setNumber(1, value)

    def getBattleBonuses(self):
        return self._getArray(2)

    def setBattleBonuses(self, value):
        self._setArray(2, value)

    @staticmethod
    def getBattleBonusesType():
        return RankedQualificationRewardsBattleBonusModel

    def _initialize(self):
        super(RankedQualificationRewardsViewModel, self)._initialize()
        self._addNumberProperty('currentProgress', 0)
        self._addNumberProperty('totalProgress', 0)
        self._addArrayProperty('battleBonuses', Array())