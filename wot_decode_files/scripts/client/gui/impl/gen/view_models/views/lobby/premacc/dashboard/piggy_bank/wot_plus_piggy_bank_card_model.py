# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/premacc/dashboard/piggy_bank/wot_plus_piggy_bank_card_model.py
from frameworks.wulf import ViewModel

class WotPlusPiggyBankCardModel(ViewModel):
    __slots__ = ('onCardClick', )

    def __init__(self, properties=7, commands=1):
        super(WotPlusPiggyBankCardModel, self).__init__(properties=properties, commands=commands)

    def getPremState(self):
        return self._getString(0)

    def setPremState(self, value):
        self._setString(0, value)

    def getCreditMaxAmount(self):
        return self._getString(1)

    def setCreditMaxAmount(self, value):
        self._setString(1, value)

    def getCreditCurrentAmount(self):
        return self._getString(2)

    def setCreditCurrentAmount(self, value):
        self._setString(2, value)

    def getWotPlusState(self):
        return self._getString(3)

    def setWotPlusState(self, value):
        self._setString(3, value)

    def getGoldMaxAmount(self):
        return self._getString(4)

    def setGoldMaxAmount(self, value):
        self._setString(4, value)

    def getGoldCurrentAmount(self):
        return self._getString(5)

    def setGoldCurrentAmount(self, value):
        self._setString(5, value)

    def getTimeToOpen(self):
        return self._getNumber(6)

    def setTimeToOpen(self, value):
        self._setNumber(6, value)

    def _initialize(self):
        super(WotPlusPiggyBankCardModel, self)._initialize()
        self._addStringProperty('premState', '')
        self._addStringProperty('creditMaxAmount', '')
        self._addStringProperty('creditCurrentAmount', '0')
        self._addStringProperty('wotPlusState', '')
        self._addStringProperty('goldMaxAmount', '')
        self._addStringProperty('goldCurrentAmount', '0')
        self._addNumberProperty('timeToOpen', 0)
        self.onCardClick = self._addCommand('onCardClick')