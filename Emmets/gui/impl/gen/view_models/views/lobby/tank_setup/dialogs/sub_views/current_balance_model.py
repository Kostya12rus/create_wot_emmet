# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/dialogs/sub_views/current_balance_model.py
from frameworks.wulf import ViewModel

class CurrentBalanceModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(CurrentBalanceModel, self).__init__(properties=properties, commands=commands)

    def getCurrencyType(self):
        return self._getString(0)

    def setCurrencyType(self, value):
        self._setString(0, value)

    def getCurrencyValue(self):
        return self._getNumber(1)

    def setCurrencyValue(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(CurrentBalanceModel, self)._initialize()
        self._addStringProperty('currencyType', '')
        self._addNumberProperty('currencyValue', 0)