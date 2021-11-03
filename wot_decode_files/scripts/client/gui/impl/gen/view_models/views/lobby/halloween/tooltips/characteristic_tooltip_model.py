# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/halloween/tooltips/characteristic_tooltip_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class RoleEnum(Enum):
    HELPER = 'helper'
    INITIATOR = 'initiator'
    UNIVERSAL = 'universal'


class CharacteristicTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(CharacteristicTooltipModel, self).__init__(properties=properties, commands=commands)

    def getRole(self):
        return RoleEnum(self._getString(0))

    def setRole(self, value):
        self._setString(0, value.value)

    def _initialize(self):
        super(CharacteristicTooltipModel, self)._initialize()
        self._addStringProperty('role')