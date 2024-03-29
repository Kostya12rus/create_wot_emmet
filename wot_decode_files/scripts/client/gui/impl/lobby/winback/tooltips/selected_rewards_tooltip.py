# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/winback/tooltips/selected_rewards_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.auxiliary.rewards_helper import BlueprintBonusTypes
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.winback.tooltips.selected_rewards_tooltip_model import SelectedRewardsTooltipModel
from gui.impl.gen.view_models.views.lobby.winback.winback_reward_view_model import RewardName
from gui.impl.lobby.winback.winback_helpers import getDiscountFromGoody, getDiscountFromBlueprint
from gui.impl.pub import ViewImpl

class SelectedRewardsTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.lobby.winback.tooltips.SelectedRewardsTooltip(), model=SelectedRewardsTooltipModel())
        settings.args = args
        settings.kwargs = kwargs
        super(SelectedRewardsTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(SelectedRewardsTooltip, self).getViewModel()

    def _onLoading(self, selectedRewards):
        super(SelectedRewardsTooltip, self)._onLoading()
        vmType = self.viewModel.getSelectedRewardsType()
        with self.viewModel.getSelectedRewards().transaction() as (tx):
            tx.clear()
            for level, reward in selectedRewards.iteritems():
                option = reward['option']
                name = option.getName()
                vm = vmType()
                vm.setVehicleLvl(level)
                vm.setName(name)
                if name == RewardName.VEHICLE_FOR_GIFT.value or name == RewardName.VEHICLE_DISCOUNT.value:
                    vm.setUserName(reward['vehicle'].userName)
                if name == RewardName.VEHICLE_DISCOUNT.value:
                    goodieId, blueprintsCount = option.getResources(reward['vehCD'])
                    vm.setCreditDiscount(getDiscountFromGoody(goodieId)[0])
                    vm.setExpDiscount(getDiscountFromBlueprint(reward['vehCD'], blueprintsCount))
                if name == BlueprintBonusTypes.BLUEPRINTS:
                    vm.setNation(option.getImageCategory())
                    vm.setCount(option.getCount())
                tx.addViewModel(vm)