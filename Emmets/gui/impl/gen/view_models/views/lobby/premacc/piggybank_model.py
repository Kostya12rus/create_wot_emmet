# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/premacc/piggybank_model.py
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.premacc.piggybank_base_model import PiggybankBaseModel

class PiggybankModel(PiggybankBaseModel):
    __slots__ = ('onPremAccProlong', 'onGoToContentPage', 'onBackBtnClicked')

    def __init__(self, properties=11, commands=3):
        super(PiggybankModel, self).__init__(properties=properties, commands=commands)

    def getPeriodInDays(self):
        return self._getNumber(6)

    def setPeriodInDays(self, value):
        self._setNumber(6, value)

    def getPiggyIsFull(self):
        return self._getBool(7)

    def setPiggyIsFull(self, value):
        self._setBool(7, value)

    def getIsPremUsed(self):
        return self._getBool(8)

    def setIsPremUsed(self, value):
        self._setBool(8, value)

    def getBackBtnLabel(self):
        return self._getResource(9)

    def setBackBtnLabel(self, value):
        self._setResource(9, value)

    def getPercentDiscount(self):
        return self._getNumber(10)

    def setPercentDiscount(self, value):
        self._setNumber(10, value)

    def _initialize(self):
        super(PiggybankModel, self)._initialize()
        self._addNumberProperty('periodInDays', 0)
        self._addBoolProperty('piggyIsFull', False)
        self._addBoolProperty('isPremUsed', False)
        self._addResourceProperty('backBtnLabel', R.invalid())
        self._addNumberProperty('percentDiscount', 0)
        self.onPremAccProlong = self._addCommand('onPremAccProlong')
        self.onGoToContentPage = self._addCommand('onGoToContentPage')
        self.onBackBtnClicked = self._addCommand('onBackBtnClicked')