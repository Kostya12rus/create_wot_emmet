# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/comp7/tooltips/season_point_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.comp7.tooltips.season_point_tooltip_model import SeasonPointTooltipModel
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

class SeasonPointTooltip(ViewImpl):
    __slots__ = ('__params', )
    __comp7Controller = dependency.descriptor(IComp7Controller)

    def __init__(self, layoutID=R.views.lobby.comp7.tooltips.SeasonPointTooltip(), params=None):
        settings = ViewSettings(layoutID)
        settings.model = SeasonPointTooltipModel()
        super(SeasonPointTooltip, self).__init__(settings)
        self.__params = params

    @property
    def viewModel(self):
        return super(SeasonPointTooltip, self).getViewModel()

    def _onLoading(self):
        super(SeasonPointTooltip, self)._onLoading()
        with self.viewModel.transaction() as (vm):
            vm.setState(self.__params['state'])
            vm.setSeasonPointExchangeRate(self.__comp7Controller.getYearlyRewards().extra.get('crystal', 0))