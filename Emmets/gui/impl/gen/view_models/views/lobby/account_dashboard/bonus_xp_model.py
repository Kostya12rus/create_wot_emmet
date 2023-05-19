# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/account_dashboard/bonus_xp_model.py
from frameworks.wulf import ViewModel

class BonusXpModel(ViewModel):
    __slots__ = ('onClick', )

    def __init__(self, properties=4, commands=1):
        super(BonusXpModel, self).__init__(properties=properties, commands=commands)

    def getIsEnabled(self):
        return self._getBool(0)

    def setIsEnabled(self, value):
        self._setBool(0, value)

    def getMultiplier(self):
        return self._getNumber(1)

    def setMultiplier(self, value):
        self._setNumber(1, value)

    def getTotalUses(self):
        return self._getNumber(2)

    def setTotalUses(self, value):
        self._setNumber(2, value)

    def getUsesLeft(self):
        return self._getNumber(3)

    def setUsesLeft(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(BonusXpModel, self)._initialize()
        self._addBoolProperty('isEnabled', True)
        self._addNumberProperty('multiplier', 1)
        self._addNumberProperty('totalUses', 0)
        self._addNumberProperty('usesLeft', 0)
        self.onClick = self._addCommand('onClick')