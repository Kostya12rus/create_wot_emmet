# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/tooltips/key_value_model.py
from frameworks.wulf import ViewModel

class KeyValueModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(KeyValueModel, self).__init__(properties=properties, commands=commands)

    def getKey(self):
        return self._getString(0)

    def setKey(self, value):
        self._setString(0, value)

    def getValue(self):
        return self._getNumber(1)

    def setValue(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(KeyValueModel, self)._initialize()
        self._addStringProperty('key', '')
        self._addNumberProperty('value', 0)