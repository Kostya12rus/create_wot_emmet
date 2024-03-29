# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle_royale/battle_results/personal/personal_results_model.py
from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.battle_royale.battle_results.personal.battle_reward_item_model import BattleRewardItemModel
from gui.impl.gen.view_models.views.battle_royale.battle_results.personal.stat_item_model import StatItemModel

class PersonalResultsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(PersonalResultsModel, self).__init__(properties=properties, commands=commands)

    def getFinishResultLabel(self):
        return self._getResource(0)

    def setFinishResultLabel(self, value):
        self._setResource(0, value)

    def getStatsList(self):
        return self._getArray(1)

    def setStatsList(self, value):
        self._setArray(1, value)

    @staticmethod
    def getStatsListType():
        return StatItemModel

    def getBattleRewardsList(self):
        return self._getArray(2)

    def setBattleRewardsList(self, value):
        self._setArray(2, value)

    @staticmethod
    def getBattleRewardsListType():
        return BattleRewardItemModel

    def getBattleRewardsListWithPremium(self):
        return self._getArray(3)

    def setBattleRewardsListWithPremium(self, value):
        self._setArray(3, value)

    @staticmethod
    def getBattleRewardsListWithPremiumType():
        return BattleRewardItemModel

    def _initialize(self):
        super(PersonalResultsModel, self)._initialize()
        self._addResourceProperty('finishResultLabel', R.invalid())
        self._addArrayProperty('statsList', Array())
        self._addArrayProperty('battleRewardsList', Array())
        self._addArrayProperty('battleRewardsListWithPremium', Array())