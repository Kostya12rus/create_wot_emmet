# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/halloween/shop_bonus_model.py
from frameworks.wulf import ViewModel

class ShopBonusModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ShopBonusModel, self).__init__(properties=properties, commands=commands)

    def getIcon(self):
        return self._getString(0)

    def setIcon(self, value):
        self._setString(0, value)

    def getAmount(self):
        return self._getNumber(1)

    def setAmount(self, value):
        self._setNumber(1, value)

    def getTooltipId(self):
        return self._getString(2)

    def setTooltipId(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(ShopBonusModel, self)._initialize()
        self._addStringProperty('icon', '')
        self._addNumberProperty('amount', 0)
        self._addStringProperty('tooltipId', '')