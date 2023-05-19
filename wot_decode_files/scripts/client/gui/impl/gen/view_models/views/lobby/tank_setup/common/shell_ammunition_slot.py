# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/common/shell_ammunition_slot.py
from gui.impl.gen.view_models.views.lobby.tank_setup.common.base_ammunition_slot import BaseAmmunitionSlot

class ShellAmmunitionSlot(BaseAmmunitionSlot):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(ShellAmmunitionSlot, self).__init__(properties=properties, commands=commands)

    def getCount(self):
        return self._getNumber(11)

    def setCount(self, value):
        self._setNumber(11, value)

    def _initialize(self):
        super(ShellAmmunitionSlot, self)._initialize()
        self._addNumberProperty('count', 0)