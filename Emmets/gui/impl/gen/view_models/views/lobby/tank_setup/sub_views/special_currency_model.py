# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/special_currency_model.py
from frameworks.wulf import ViewModel

class SpecialCurrencyModel(ViewModel):
    __slots__ = ('onGetMoreCurrency', )

    def __init__(self, properties=2, commands=1):
        super(SpecialCurrencyModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getValue(self):
        return self._getReal(1)

    def setValue(self, value):
        self._setReal(1, value)

    def _initialize(self):
        super(SpecialCurrencyModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addRealProperty('value', 0.0)
        self.onGetMoreCurrency = self._addCommand('onGetMoreCurrency')