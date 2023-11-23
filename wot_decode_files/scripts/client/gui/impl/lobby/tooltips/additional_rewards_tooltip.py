# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tooltips/additional_rewards_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.tooltips.additional_rewards_tooltip_model import AdditionalRewardsTooltipModel
from gui.impl.pub import ViewImpl

class AdditionalRewardsTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.lobby.tooltips.AdditionalRewardsTooltip())
        settings.model = AdditionalRewardsTooltipModel()
        settings.args = args
        settings.kwargs = kwargs
        super(AdditionalRewardsTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(AdditionalRewardsTooltip, self).getViewModel()

    def _onLoading(self, packedBonuses, *args, **kwargs):
        super(AdditionalRewardsTooltip, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as (model):
            model.setHeaderText(R.strings.tooltips.quests.awards.additional.header())
            model.setHeaderCount(0)
            model.setDescription(R.invalid())
            model.setDescriptionCount(0)
            bonusArray = model.getBonus()
            bonusArray.clear()
            for item in packedBonuses:
                bonusArray.addViewModel(item)

            bonusArray.invalidate()