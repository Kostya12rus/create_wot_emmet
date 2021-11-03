# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/tooltips/battle_pass_in_progress_tooltip_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.battle_royale_reward_points import BattleRoyaleRewardPoints
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.reward_points_model import RewardPointsModel

class BattlePassInProgressTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(BattlePassInProgressTooltipViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def rewardPoints(self):
        return self._getViewModel(0)

    @property
    def battleRoyaleRewardPoints(self):
        return self._getViewModel(1)

    @property
    def rewardsCommon(self):
        return self._getViewModel(2)

    @property
    def rewardsElite(self):
        return self._getViewModel(3)

    def getLevel(self):
        return self._getNumber(4)

    def setLevel(self, value):
        self._setNumber(4, value)

    def getChapter(self):
        return self._getNumber(5)

    def setChapter(self, value):
        self._setNumber(5, value)

    def getCurrentPoints(self):
        return self._getNumber(6)

    def setCurrentPoints(self, value):
        self._setNumber(6, value)

    def getMaxPoints(self):
        return self._getNumber(7)

    def setMaxPoints(self, value):
        self._setNumber(7, value)

    def getIsBattlePassPurchased(self):
        return self._getBool(8)

    def setIsBattlePassPurchased(self, value):
        self._setBool(8, value)

    def getTimeTillEnd(self):
        return self._getString(9)

    def setTimeTillEnd(self, value):
        self._setString(9, value)

    def getBattleType(self):
        return self._getString(10)

    def setBattleType(self, value):
        self._setString(10, value)

    def getNotChosenRewardCount(self):
        return self._getNumber(11)

    def setNotChosenRewardCount(self, value):
        self._setNumber(11, value)

    def _initialize(self):
        super(BattlePassInProgressTooltipViewModel, self)._initialize()
        self._addViewModelProperty('rewardPoints', UserListModel())
        self._addViewModelProperty('battleRoyaleRewardPoints', BattleRoyaleRewardPoints())
        self._addViewModelProperty('rewardsCommon', UserListModel())
        self._addViewModelProperty('rewardsElite', UserListModel())
        self._addNumberProperty('level', 0)
        self._addNumberProperty('chapter', 0)
        self._addNumberProperty('currentPoints', 0)
        self._addNumberProperty('maxPoints', 0)
        self._addBoolProperty('isBattlePassPurchased', False)
        self._addStringProperty('timeTillEnd', '')
        self._addStringProperty('battleType', '')
        self._addNumberProperty('notChosenRewardCount', 0)