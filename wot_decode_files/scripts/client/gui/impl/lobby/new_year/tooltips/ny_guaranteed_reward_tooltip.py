# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/new_year/tooltips/ny_guaranteed_reward_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen.view_models.views.lobby.new_year.tooltips.ny_guaranteed_reward_tooltip_model import NyGuaranteedRewardTooltipModel
from gui.impl.pub import ViewImpl
from gui.impl.gen import R

class NyGuaranteedRewardTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self):
        settings = ViewSettings(R.views.lobby.new_year.tooltips.NyGuaranteedRewardTooltip())
        settings.model = NyGuaranteedRewardTooltipModel()
        super(NyGuaranteedRewardTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(NyGuaranteedRewardTooltip, self).getViewModel()