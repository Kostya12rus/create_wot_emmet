# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/new_year/tooltips/ny_total_bonus_tooltip.py
from frameworks.wulf import View, ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.tooltips.ny_total_bonus_tooltip_model import NyTotalBonusTooltipModel
from new_year.ny_bonuses import CreditsBonusHelper
from gui.impl.new_year.new_year_helper import fillBonusFormula
from shared_utils import inPercents
from skeletons.new_year import INewYearController
from helpers import dependency

class NyTotalBonusTooltip(View):
    __slots__ = ()
    _nyController = dependency.descriptor(INewYearController)

    def __init__(self):
        super(NyTotalBonusTooltip, self).__init__(ViewSettings(R.views.lobby.new_year.tooltips.NyTotalBonusTooltip(), model=NyTotalBonusTooltipModel()))

    @property
    def viewModel(self):
        return super(NyTotalBonusTooltip, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        fillBonusFormula(self.viewModel.bonusFormula)
        with self.viewModel.transaction() as (tx):
            tx.setMaxBonus(inPercents(CreditsBonusHelper.getMaxBonus(), digitsToRound=0))
            tx.setCreditsBonus(inPercents(self._nyController.getActiveSettingBonusValue()))
            tx.setIsPostNYEnabled(self._nyController.isPostEvent())