# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/dialogs/sub_views/event_price_view_model.py
from frameworks.wulf import ViewModel

class EventPriceViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(EventPriceViewModel, self).__init__(properties=properties, commands=commands)

    def getText(self):
        return self._getString(0)

    def setText(self, value):
        self._setString(0, value)

    def getCount(self):
        return self._getNumber(1)

    def setCount(self, value):
        self._setNumber(1, value)

    def getCurrencyType(self):
        return self._getString(2)

    def setCurrencyType(self, value):
        self._setString(2, value)

    def getIsEnought(self):
        return self._getBool(3)

    def setIsEnought(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(EventPriceViewModel, self)._initialize()
        self._addStringProperty('text', '')
        self._addNumberProperty('count', 0)
        self._addStringProperty('currencyType', '')
        self._addBoolProperty('isEnought', False)