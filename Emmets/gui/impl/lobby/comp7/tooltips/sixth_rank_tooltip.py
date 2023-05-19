# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/comp7/tooltips/sixth_rank_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.comp7.tooltips.sixth_rank_tooltip_model import SixthRankTooltipModel
from gui.impl.lobby.comp7.meta_view.meta_view_helper import getRankDivisions
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext

class SixthRankTooltip(ViewImpl):
    __slots__ = ()
    __lobbyCtx = dependency.descriptor(ILobbyContext)

    def __init__(self, layoutID=R.views.lobby.comp7.tooltips.SixthRankTooltip()):
        settings = ViewSettings(layoutID)
        settings.model = SixthRankTooltipModel()
        super(SixthRankTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(SixthRankTooltip, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        super(SixthRankTooltip, self)._initialize(*args, **kwargs)
        ranksConfig = self.__lobbyCtx.getServerSettings().comp7PrestigeRanksConfig
        divisions = getRankDivisions(6, ranksConfig)
        self.viewModel.setFrom(divisions[0].range.begin)