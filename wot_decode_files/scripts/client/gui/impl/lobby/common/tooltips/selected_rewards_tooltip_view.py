# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/common/tooltips/selected_rewards_tooltip_view.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.common.tooltips.selected_rewards_tooltip_category_model import SelectedRewardsTooltipCategoryModel
from gui.impl.gen.view_models.views.lobby.common.tooltips.selected_rewards_tooltip_reward_model import SelectedRewardsTooltipRewardModel
from gui.impl.gen.view_models.views.lobby.common.tooltips.selected_rewards_tooltip_view_model import SelectedRewardsTooltipViewModel
from gui.impl.pub import ViewImpl

class SelectedRewardsTooltipView(ViewImpl):
    __slots__ = ('__cart', '__count')

    def __init__(self, cart, count):
        settings = ViewSettings(R.views.lobby.common.tooltips.SelectedRewardsTooltipView())
        settings.model = SelectedRewardsTooltipViewModel()
        self.__cart = cart
        self.__count = count
        super(SelectedRewardsTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(SelectedRewardsTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        with self.viewModel.transaction() as (tx):
            tx.setTotalSelected(self.__count)
            categories = tx.getCategories()
            categories.clear()
            for tabName, tabContent in self.__cart.iteritems():
                newCategory = SelectedRewardsTooltipCategoryModel()
                newCategory.setType(tabName)
                rewards = newCategory.getRewards()
                rewards.clear()
                for rewardName, rewardList in tabContent.iteritems():
                    newReward = SelectedRewardsTooltipRewardModel()
                    newReward.setType(rewardName)
                    newReward.setCount(len(rewardList) * rewardList[0]['packSize'])
                    rewards.addViewModel(newReward)

                categories.addViewModel(newCategory)