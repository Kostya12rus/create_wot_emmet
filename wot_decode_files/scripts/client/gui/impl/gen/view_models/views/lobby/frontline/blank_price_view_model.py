# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/frontline/blank_price_view_model.py
from frameworks.wulf import ViewModel

class BlankPriceViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BlankPriceViewModel, self).__init__(properties=properties, commands=commands)

    def getTooltipId(self):
        return self._getString(0)

    def setTooltipId(self, value):
        self._setString(0, value)

    def getCount(self):
        return self._getNumber(1)

    def setCount(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(BlankPriceViewModel, self)._initialize()
        self._addStringProperty('tooltipId', '')
        self._addNumberProperty('count', 0)