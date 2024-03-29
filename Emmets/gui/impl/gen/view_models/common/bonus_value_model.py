# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/bonus_value_model.py
from frameworks.wulf import ViewModel

class BonusValueModel(ViewModel):
    __slots__ = ()
    MUL_VALUE = 'mul'

    def __init__(self, properties=4, commands=0):
        super(BonusValueModel, self).__init__(properties=properties, commands=commands)

    def getValueKey(self):
        return self._getString(0)

    def setValueKey(self, value):
        self._setString(0, value)

    def getValue(self):
        return self._getReal(1)

    def setValue(self, value):
        self._setReal(1, value)

    def getValueType(self):
        return self._getString(2)

    def setValueType(self, value):
        self._setString(2, value)

    def getIsDebuff(self):
        return self._getBool(3)

    def setIsDebuff(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(BonusValueModel, self)._initialize()
        self._addStringProperty('valueKey', '')
        self._addRealProperty('value', 0.0)
        self._addStringProperty('valueType', 'mul')
        self._addBoolProperty('isDebuff', False)