# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/winback/tooltips/selectable_reward_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.winback.tooltips.selectable_reward_tooltip_model import SelectableRewardTooltipModel
from gui.impl.pub import ViewImpl

class SelectableRewardTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.lobby.winback.tooltips.SelectableRewardTooltip(), model=SelectableRewardTooltipModel())
        settings.args = args
        settings.kwargs = kwargs
        super(SelectableRewardTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(SelectableRewardTooltip, self).getViewModel()

    def _onLoading(self, level, isDiscount, researchDiscount, purchaseDiscount):
        super(SelectableRewardTooltip, self)._onLoading()
        self.viewModel.setLevel(level)
        self.viewModel.setIsDiscount(isDiscount)
        self.viewModel.setResearchDiscount(researchDiscount)
        self.viewModel.setPurchaseDiscount(purchaseDiscount)