# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle/battle_page/prebattle_shell_ammunition_slot.py
from enum import IntEnum
from gui.impl.gen.view_models.views.lobby.tank_setup.common.shell_ammunition_slot import ShellAmmunitionSlot

class ShellBattleState(IntEnum):
    NORMAL = 0
    CURRENT = 1
    NEXT = 2


class PrebattleShellAmmunitionSlot(ShellAmmunitionSlot):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(PrebattleShellAmmunitionSlot, self).__init__(properties=properties, commands=commands)

    def getShellState(self):
        return ShellBattleState(self._getNumber(12))

    def setShellState(self, value):
        self._setNumber(12, value.value)

    def _initialize(self):
        super(PrebattleShellAmmunitionSlot, self)._initialize()
        self._addNumberProperty('shellState')