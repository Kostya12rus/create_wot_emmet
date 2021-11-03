# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/halloween/price_model.py
from frameworks.wulf import ViewModel

class PriceModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(PriceModel, self).__init__(properties=properties, commands=commands)

    def getValue(self):
        return self._getNumber(0)

    def setValue(self, value):
        self._setNumber(0, value)

    def getOldValue(self):
        return self._getNumber(1)

    def setOldValue(self, value):
        self._setNumber(1, value)

    def getIsEnough(self):
        return self._getBool(2)

    def setIsEnough(self, value):
        self._setBool(2, value)

    def getDiscountValue(self):
        return self._getNumber(3)

    def setDiscountValue(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(PriceModel, self)._initialize()
        self._addNumberProperty('value', 0)
        self._addNumberProperty('oldValue', 0)
        self._addBoolProperty('isEnough', False)
        self._addNumberProperty('discountValue', 0)