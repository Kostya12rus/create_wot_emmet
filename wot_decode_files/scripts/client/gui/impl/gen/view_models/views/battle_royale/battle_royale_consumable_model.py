# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle_royale/battle_royale_consumable_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class BattleRoyaleConsumableModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(BattleRoyaleConsumableModel, self).__init__(properties=properties, commands=commands)

    def getIconSource(self):
        return self._getResource(0)

    def setIconSource(self, value):
        self._setResource(0, value)

    def getQuantity(self):
        return self._getNumber(1)

    def setQuantity(self, value):
        self._setNumber(1, value)

    def getIntCD(self):
        return self._getNumber(2)

    def setIntCD(self, value):
        self._setNumber(2, value)

    def getTooltipType(self):
        return self._getString(3)

    def setTooltipType(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(BattleRoyaleConsumableModel, self)._initialize()
        self._addResourceProperty('iconSource', R.invalid())
        self._addNumberProperty('quantity', 0)
        self._addNumberProperty('intCD', 0)
        self._addStringProperty('tooltipType', '')