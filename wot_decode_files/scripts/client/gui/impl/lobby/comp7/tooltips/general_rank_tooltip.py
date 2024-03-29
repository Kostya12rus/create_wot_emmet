# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/comp7/tooltips/general_rank_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.comp7.tooltips.general_rank_tooltip_model import GeneralRankTooltipModel
from gui.impl.pub import ViewImpl

class GeneralRankTooltip(ViewImpl):
    __slots__ = ('__params', )

    def __init__(self, layoutID=R.views.lobby.comp7.tooltips.GeneralRankTooltip(), params=None):
        settings = ViewSettings(layoutID)
        settings.model = GeneralRankTooltipModel()
        super(GeneralRankTooltip, self).__init__(settings)
        self.__params = params

    @property
    def viewModel(self):
        return super(GeneralRankTooltip, self).getViewModel()

    def _onLoading(self):
        super(GeneralRankTooltip, self)._onLoading()
        with self.viewModel.transaction() as (vm):
            vm.setRank(self.__params['rank'])
            vm.setDivisions(self.__params['divisions'])
            vm.setFrom(self.__params['from'])
            vm.setTo(self.__params['to'])