# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/comp7/year_model.py
from enum import IntEnum
from frameworks.wulf import ViewModel

class YearState(IntEnum):
    NOTSTARTED = 0
    ACTIVE = 1
    OFFSEASON = 3
    FINISHED = 4


class YearModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(YearModel, self).__init__(properties=properties, commands=commands)

    def getState(self):
        return YearState(self._getNumber(0))

    def setState(self, value):
        self._setNumber(0, value.value)

    def _initialize(self):
        super(YearModel, self)._initialize()
        self._addNumberProperty('state')