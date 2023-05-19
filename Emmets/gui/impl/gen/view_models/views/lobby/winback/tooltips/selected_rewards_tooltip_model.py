# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/winback/tooltips/selected_rewards_tooltip_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.winback.tooltips.selected_reward_model import SelectedRewardModel

class SelectedRewardsTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(SelectedRewardsTooltipModel, self).__init__(properties=properties, commands=commands)

    def getSelectedRewards(self):
        return self._getArray(0)

    def setSelectedRewards(self, value):
        self._setArray(0, value)

    @staticmethod
    def getSelectedRewardsType():
        return SelectedRewardModel

    def _initialize(self):
        super(SelectedRewardsTooltipModel, self)._initialize()
        self._addArrayProperty('selectedRewards', Array())