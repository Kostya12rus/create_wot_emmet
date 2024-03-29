# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/currency_reserves/currency_reserve_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class CurrencyEnum(Enum):
    CREDITS = 'Credits'
    GOLD = 'Gold'


class CurrencyReserveModel(ViewModel):
    __slots__ = ('onInfoButtonClick', 'onActionButtonClick')

    def __init__(self, properties=5, commands=2):
        super(CurrencyReserveModel, self).__init__(properties=properties, commands=commands)

    def getCurrency(self):
        return CurrencyEnum(self._getString(0))

    def setCurrency(self, value):
        self._setString(0, value.value)

    def getMaxCapacity(self):
        return self._getNumber(1)

    def setMaxCapacity(self, value):
        self._setNumber(1, value)

    def getAmount(self):
        return self._getNumber(2)

    def setAmount(self, value):
        self._setNumber(2, value)

    def getIsActive(self):
        return self._getBool(3)

    def setIsActive(self, value):
        self._setBool(3, value)

    def getIsEnabled(self):
        return self._getBool(4)

    def setIsEnabled(self, value):
        self._setBool(4, value)

    def _initialize(self):
        super(CurrencyReserveModel, self)._initialize()
        self._addStringProperty('currency')
        self._addNumberProperty('maxCapacity', 0)
        self._addNumberProperty('amount', 0)
        self._addBoolProperty('isActive', False)
        self._addBoolProperty('isEnabled', True)
        self.onInfoButtonClick = self._addCommand('onInfoButtonClick')
        self.onActionButtonClick = self._addCommand('onActionButtonClick')