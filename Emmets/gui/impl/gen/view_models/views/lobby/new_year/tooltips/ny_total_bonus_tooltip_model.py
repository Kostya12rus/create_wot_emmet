# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/new_year/tooltips/ny_total_bonus_tooltip_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.new_year.tooltips.ny_bonus_formula_model import NyBonusFormulaModel

class NyTotalBonusTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(NyTotalBonusTooltipModel, self).__init__(properties=properties, commands=commands)

    @property
    def bonusFormula(self):
        return self._getViewModel(0)

    def getCreditsBonus(self):
        return self._getReal(1)

    def setCreditsBonus(self, value):
        self._setReal(1, value)

    def getMaxBonus(self):
        return self._getReal(2)

    def setMaxBonus(self, value):
        self._setReal(2, value)

    def getIsPostNYEnabled(self):
        return self._getBool(3)

    def setIsPostNYEnabled(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(NyTotalBonusTooltipModel, self)._initialize()
        self._addViewModelProperty('bonusFormula', NyBonusFormulaModel())
        self._addRealProperty('creditsBonus', 0.0)
        self._addRealProperty('maxBonus', 50)
        self._addBoolProperty('isPostNYEnabled', False)