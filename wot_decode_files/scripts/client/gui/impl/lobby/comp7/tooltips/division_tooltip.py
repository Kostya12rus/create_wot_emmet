# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/comp7/tooltips/division_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.comp7.tooltips.division_tooltip_model import DivisionTooltipModel
from gui.impl.pub import ViewImpl

class DivisionTooltip(ViewImpl):
    __slots__ = ('__params', )

    def __init__(self, layoutID=R.views.lobby.comp7.tooltips.DivisionTooltip(), params=None):
        settings = ViewSettings(layoutID)
        settings.model = DivisionTooltipModel()
        super(DivisionTooltip, self).__init__(settings)
        self.__params = params

    @property
    def viewModel(self):
        return super(DivisionTooltip, self).getViewModel()

    def _onLoading(self):
        super(DivisionTooltip, self)._onLoading()
        with self.viewModel.transaction() as (vm):
            vm.setRank(self.__params['rank'])
            vm.setDivision(self.__params['division'])
            vm.setFrom(self.__params['from'])
            vm.setTo(self.__params['to'])