# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/new_year/tooltips/ny_bonus_formula_model.py
from frameworks.wulf import ViewModel

class NyBonusFormulaModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(NyBonusFormulaModel, self).__init__(properties=properties, commands=commands)

    def getCreditsBonus(self):
        return self._getReal(0)

    def setCreditsBonus(self, value):
        self._setReal(0, value)

    def getCollectionBonus(self):
        return self._getReal(1)

    def setCollectionBonus(self, value):
        self._setReal(1, value)

    def getMegaBonus(self):
        return self._getReal(2)

    def setMegaBonus(self, value):
        self._setReal(2, value)

    def getMultiplier(self):
        return self._getNumber(3)

    def setMultiplier(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(NyBonusFormulaModel, self)._initialize()
        self._addRealProperty('creditsBonus', 0.0)
        self._addRealProperty('collectionBonus', 0.0)
        self._addRealProperty('megaBonus', 0.0)
        self._addNumberProperty('multiplier', 1)