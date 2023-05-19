# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/value_price.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class ValuePrice(ViewModel):
    __slots__ = ()
    CUSTOM = 'custom'
    CREDITS = 'credits'
    GOLD = 'gold'
    EXP = 'exp'
    FREE_XP = 'freeXP'
    CRYSTAL = 'crystal'

    def __init__(self, properties=4, commands=0):
        super(ValuePrice, self).__init__(properties=properties, commands=commands)

    def getValue(self):
        return self._getString(0)

    def setValue(self, value):
        self._setString(0, value)

    def getType(self):
        return self._getString(1)

    def setType(self, value):
        self._setString(1, value)

    def getIcon(self):
        return self._getResource(2)

    def setIcon(self, value):
        self._setResource(2, value)

    def getNotEnough(self):
        return self._getBool(3)

    def setNotEnough(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(ValuePrice, self)._initialize()
        self._addStringProperty('value', '0')
        self._addStringProperty('type', 'custom')
        self._addResourceProperty('icon', R.invalid())
        self._addBoolProperty('notEnough', False)