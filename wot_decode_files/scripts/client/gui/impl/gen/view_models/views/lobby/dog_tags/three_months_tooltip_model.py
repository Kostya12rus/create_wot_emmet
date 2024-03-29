# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/dog_tags/three_months_tooltip_model.py
from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class ThreeMonthsTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(ThreeMonthsTooltipModel, self).__init__(properties=properties, commands=commands)

    def getHighlightedIndex(self):
        return self._getNumber(0)

    def setHighlightedIndex(self, value):
        self._setNumber(0, value)

    def getMonthlyValues(self):
        return self._getArray(1)

    def setMonthlyValues(self, value):
        self._setArray(1, value)

    def getMonthNames(self):
        return self._getArray(2)

    def setMonthNames(self, value):
        self._setArray(2, value)

    def getCurrentMonth(self):
        return self._getResource(3)

    def setCurrentMonth(self, value):
        self._setResource(3, value)

    def getProgressNumberType(self):
        return self._getString(4)

    def setProgressNumberType(self, value):
        self._setString(4, value)

    def _initialize(self):
        super(ThreeMonthsTooltipModel, self)._initialize()
        self._addNumberProperty('highlightedIndex', 0)
        self._addArrayProperty('monthlyValues', Array())
        self._addArrayProperty('monthNames', Array())
        self._addResourceProperty('currentMonth', R.invalid())
        self._addStringProperty('progressNumberType', '')