# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/price_item_model.py
from frameworks.wulf import ViewModel

class PriceItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PriceItemModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getValue(self):
        return self._getReal(1)

    def setValue(self, value):
        self._setReal(1, value)

    def getIsEnough(self):
        return self._getBool(2)

    def setIsEnough(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(PriceItemModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addRealProperty('value', 0.0)
        self._addBoolProperty('isEnough', True)