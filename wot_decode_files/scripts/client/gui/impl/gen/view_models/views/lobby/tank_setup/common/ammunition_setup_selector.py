# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/common/ammunition_setup_selector.py
from enum import IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class SetupStates(IntEnum):
    NORMAL = 0
    WARNING = 1


class AmmunitionSetupSelector(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(AmmunitionSetupSelector, self).__init__(properties=properties, commands=commands)

    def getIsSwitchEnabled(self):
        return self._getBool(0)

    def setIsSwitchEnabled(self, value):
        self._setBool(0, value)

    def getIsPrebattleSwitchDisabled(self):
        return self._getBool(1)

    def setIsPrebattleSwitchDisabled(self, value):
        self._setBool(1, value)

    def getStates(self):
        return self._getArray(2)

    def setStates(self, value):
        self._setArray(2, value)

    @staticmethod
    def getStatesType():
        return int

    def _initialize(self):
        super(AmmunitionSetupSelector, self)._initialize()
        self._addBoolProperty('isSwitchEnabled', False)
        self._addBoolProperty('isPrebattleSwitchDisabled', False)
        self._addArrayProperty('states', Array())