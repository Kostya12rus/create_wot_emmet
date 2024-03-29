# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/marathon/marathon_reward_tooltip_content.py
from frameworks.wulf import ViewSettings
from gui.impl.pub import ViewImpl
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.marathon.marathon_rest_reward_tooltip_model import MarathonRestRewardTooltipModel

class MarathonRewardTooltipContent(ViewImpl):

    def __init__(self, rewards):
        settings = ViewSettings(R.views.lobby.marathon.tooltips.RestRewardTooltip())
        settings.model = MarathonRestRewardTooltipModel()
        super(MarathonRewardTooltipContent, self).__init__(settings)
        self.__rewards = rewards

    @property
    def viewModel(self):
        return self.getViewModel()

    def _onLoading(self, *args, **kwargs):
        self.viewModel.setRewards(self.__rewards)