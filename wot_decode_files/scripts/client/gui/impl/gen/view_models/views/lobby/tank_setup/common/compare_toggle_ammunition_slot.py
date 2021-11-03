# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/common/compare_toggle_ammunition_slot.py
from gui.impl.gen.view_models.views.lobby.tank_setup.common.base_ammunition_slot import BaseAmmunitionSlot

class CompareToggleAmmunitionSlot(BaseAmmunitionSlot):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(CompareToggleAmmunitionSlot, self).__init__(properties=properties, commands=commands)

    def getIsSelected(self):
        return self._getBool(11)

    def setIsSelected(self, value):
        self._setBool(11, value)

    def getIsLocked(self):
        return self._getBool(12)

    def setIsLocked(self, value):
        self._setBool(12, value)

    def _initialize(self):
        super(CompareToggleAmmunitionSlot, self)._initialize()
        self._addBoolProperty('isSelected', False)
        self._addBoolProperty('isLocked', False)