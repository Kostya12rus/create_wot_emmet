# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/freeXp_book_model.py
from frameworks.wulf import ViewModel

class FreeXpBookModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(FreeXpBookModel, self).__init__(properties=properties, commands=commands)

    def getPlayerXp(self):
        return self._getNumber(0)

    def setPlayerXp(self, value):
        self._setNumber(0, value)

    def getDiscountSize(self):
        return self._getNumber(1)

    def setDiscountSize(self, value):
        self._setNumber(1, value)

    def getCurrentXpValue(self):
        return self._getNumber(2)

    def setCurrentXpValue(self, value):
        self._setNumber(2, value)

    def getCurrentMaxValue(self):
        return self._getNumber(3)

    def setCurrentMaxValue(self, value):
        self._setNumber(3, value)

    def getExchangeRate(self):
        return self._getNumber(4)

    def setExchangeRate(self, value):
        self._setNumber(4, value)

    def getIsEligibleToApplyFreeXp(self):
        return self._getBool(5)

    def setIsEligibleToApplyFreeXp(self, value):
        self._setBool(5, value)

    def _initialize(self):
        super(FreeXpBookModel, self)._initialize()
        self._addNumberProperty('playerXp', 0)
        self._addNumberProperty('discountSize', 0)
        self._addNumberProperty('currentXpValue', 0)
        self._addNumberProperty('currentMaxValue', 0)
        self._addNumberProperty('exchangeRate', 1)
        self._addBoolProperty('isEligibleToApplyFreeXp', False)