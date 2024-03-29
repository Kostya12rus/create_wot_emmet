# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/platoon/bonus_model.py
from frameworks.wulf import ViewModel

class BonusModel(ViewModel):
    __slots__ = ()
    GOLD = 'gold'
    CREDITS = 'credits'
    CRYSTAL = 'crystal'
    XP = 'xp'
    FREE_XP = 'freeXP'

    def __init__(self, properties=2, commands=0):
        super(BonusModel, self).__init__(properties=properties, commands=commands)

    def getCurrency(self):
        return self._getString(0)

    def setCurrency(self, value):
        self._setString(0, value)

    def getAmount(self):
        return self._getNumber(1)

    def setAmount(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(BonusModel, self)._initialize()
        self._addStringProperty('currency', '')
        self._addNumberProperty('amount', 0)