# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/comp7/tooltips/seventh_rank_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.comp7.tooltips.seventh_rank_tooltip_model import SeventhRankTooltipModel
from gui.impl.lobby.comp7 import comp7_model_helpers
from gui.impl.pub import ViewImpl

class SeventhRankTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self, layoutID=R.views.lobby.comp7.tooltips.SeventhRankTooltip()):
        settings = ViewSettings(layoutID)
        settings.model = SeventhRankTooltipModel()
        super(SeventhRankTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(SeventhRankTooltip, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        super(SeventhRankTooltip, self)._initialize(*args, **kwargs)
        comp7_model_helpers.setElitePercentage(self.viewModel)