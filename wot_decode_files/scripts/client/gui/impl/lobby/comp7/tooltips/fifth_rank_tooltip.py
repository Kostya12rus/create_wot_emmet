# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/comp7/tooltips/fifth_rank_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.comp7.tooltips.fifth_rank_tooltip_model import FifthRankTooltipModel
from gui.impl.lobby.comp7.meta_view.meta_view_helper import getRankDivisions
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext

class FifthRankTooltip(ViewImpl):
    __slots__ = ()
    __lobbyCtx = dependency.descriptor(ILobbyContext)

    def __init__(self, layoutID=R.views.lobby.comp7.tooltips.FifthRankTooltip()):
        settings = ViewSettings(layoutID)
        settings.model = FifthRankTooltipModel()
        super(FifthRankTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(FifthRankTooltip, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        super(FifthRankTooltip, self)._initialize(*args, **kwargs)
        ranksConfig = self.__lobbyCtx.getServerSettings().comp7RanksConfig
        divisions = getRankDivisions(2, ranksConfig)
        self.viewModel.setFrom(divisions[0].range.begin)