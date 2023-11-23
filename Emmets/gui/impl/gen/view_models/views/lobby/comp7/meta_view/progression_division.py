# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/comp7/meta_view/progression_division.py
from enum import IntEnum
from frameworks.wulf import ViewModel

class Division(IntEnum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5


class State(IntEnum):
    ACHIEVED = 0
    CURRENT = 1
    INACTIVE = 2


class ProgressionDivision(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ProgressionDivision, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return Division(self._getNumber(0))

    def setName(self, value):
        self._setNumber(0, value.value)

    def getState(self):
        return State(self._getNumber(1))

    def setState(self, value):
        self._setNumber(1, value.value)

    def _initialize(self):
        super(ProgressionDivision, self)._initialize()
        self._addNumberProperty('name')
        self._addNumberProperty('state')