# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/common/battle_ability_ammunition_slot.py
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.tank_setup.common.base_ammunition_slot import BaseAmmunitionSlot

class BattleAbilityAmmunitionSlot(BaseAmmunitionSlot):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(BattleAbilityAmmunitionSlot, self).__init__(properties=properties, commands=commands)

    def getLevel(self):
        return self._getNumber(11)

    def setLevel(self, value):
        self._setNumber(11, value)

    def getRank(self):
        return self._getResource(12)

    def setRank(self, value):
        self._setResource(12, value)

    def _initialize(self):
        super(BattleAbilityAmmunitionSlot, self)._initialize()
        self._addNumberProperty('level', 0)
        self._addResourceProperty('rank', R.invalid())