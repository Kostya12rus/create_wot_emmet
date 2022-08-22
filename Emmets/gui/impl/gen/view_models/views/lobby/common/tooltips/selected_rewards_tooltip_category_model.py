# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/common/tooltips/selected_rewards_tooltip_category_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.common.tooltips.selected_rewards_tooltip_reward_model import SelectedRewardsTooltipRewardModel

class SelectedRewardsTooltipCategoryModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(SelectedRewardsTooltipCategoryModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)

    @staticmethod
    def getRewardsType():
        return SelectedRewardsTooltipRewardModel

    def _initialize(self):
        super(SelectedRewardsTooltipCategoryModel, self)._initialize()
        self._addStringProperty('type', '')
        self._addArrayProperty('rewards', Array())