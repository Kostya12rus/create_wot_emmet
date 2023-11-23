# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle_royale/proxy_currency_cmp_view_model.py
from frameworks.wulf import ViewModel

class ProxyCurrencyCmpViewModel(ViewModel):
    __slots__ = ('onGotoShopBtnClicked', )

    def __init__(self, properties=1, commands=1):
        super(ProxyCurrencyCmpViewModel, self).__init__(properties=properties, commands=commands)

    def getBalance(self):
        return self._getNumber(0)

    def setBalance(self, value):
        self._setNumber(0, value)

    def _initialize(self):
        super(ProxyCurrencyCmpViewModel, self)._initialize()
        self._addNumberProperty('balance', 0)
        self.onGotoShopBtnClicked = self._addCommand('onGotoShopBtnClicked')