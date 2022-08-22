# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/ranked/ranked_qualification_rewards_battle_bonus_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel

class RankedQualificationRewardsBattleBonusModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(RankedQualificationRewardsBattleBonusModel, self).__init__(properties=properties, commands=commands)

    def getBattlesCount(self):
        return self._getNumber(0)

    def setBattlesCount(self, value):
        self._setNumber(0, value)

    def getBonuses(self):
        return self._getArray(1)

    def setBonuses(self, value):
        self._setArray(1, value)

    @staticmethod
    def getBonusesType():
        return RewardItemModel

    def _initialize(self):
        super(RankedQualificationRewardsBattleBonusModel, self)._initialize()
        self._addNumberProperty('battlesCount', 0)
        self._addArrayProperty('bonuses', Array())