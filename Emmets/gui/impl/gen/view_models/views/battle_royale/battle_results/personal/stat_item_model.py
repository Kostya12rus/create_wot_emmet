# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle_royale/battle_results/personal/stat_item_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class StatItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(StatItemModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)

    def getWreathImage(self):
        return self._getResource(1)

    def setWreathImage(self, value):
        self._setResource(1, value)

    def getCurrentValue(self):
        return self._getNumber(2)

    def setCurrentValue(self, value):
        self._setNumber(2, value)

    def getMaxValue(self):
        return self._getNumber(3)

    def setMaxValue(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(StatItemModel, self)._initialize()
        self._addStringProperty('type', '')
        self._addResourceProperty('wreathImage', R.invalid())
        self._addNumberProperty('currentValue', -1)
        self._addNumberProperty('maxValue', -1)