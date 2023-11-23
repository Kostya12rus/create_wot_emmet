# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/comp7/tooltips/sixth_rank_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.comp7.tooltips.sixth_rank_tooltip_model import SixthRankTooltipModel
from gui.impl.lobby.comp7 import comp7_model_helpers
from gui.impl.pub import ViewImpl

class SixthRankTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self, layoutID=R.views.lobby.comp7.tooltips.SixthRankTooltip()):
        settings = ViewSettings(layoutID)
        settings.model = SixthRankTooltipModel()
        super(SixthRankTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(SixthRankTooltip, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        super(SixthRankTooltip, self)._initialize(*args, **kwargs)
        comp7_model_helpers.setElitePercentage(self.viewModel)