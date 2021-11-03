# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/simple_price_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class PriceTypeEnum(Enum):
    CREDITS = 'credits'
    GOLD = 'gold'
    CRYSTAL = 'crystal'
    TOKENS = 'tokens'


class SimplePriceModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(SimplePriceModel, self).__init__(properties=properties, commands=commands)

    def getValue(self):
        return self._getNumber(0)

    def setValue(self, value):
        self._setNumber(0, value)

    def getType(self):
        return PriceTypeEnum(self._getString(1))

    def setType(self, value):
        self._setString(1, value.value)

    def getIsEnough(self):
        return self._getBool(2)

    def setIsEnough(self, value):
        self._setBool(2, value)

    def getHasDiscount(self):
        return self._getBool(3)

    def setHasDiscount(self, value):
        self._setBool(3, value)

    def getDiscountValue(self):
        return self._getReal(4)

    def setDiscountValue(self, value):
        self._setReal(4, value)

    def _initialize(self):
        super(SimplePriceModel, self)._initialize()
        self._addNumberProperty('value', 0)
        self._addStringProperty('type')
        self._addBoolProperty('isEnough', False)
        self._addBoolProperty('hasDiscount', False)
        self._addRealProperty('discountValue', 0.0)