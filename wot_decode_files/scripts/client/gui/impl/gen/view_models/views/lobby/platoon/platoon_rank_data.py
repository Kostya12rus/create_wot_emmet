# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/platoon/platoon_rank_data.py
from enum import IntEnum
from frameworks.wulf import ViewModel

class Rank(IntEnum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5
    SIXTH = 6
    SEVENTH = 7


class Division(IntEnum):
    A = 0
    B = 1
    C = 2
    D = 3


class PlatoonRankData(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PlatoonRankData, self).__init__(properties=properties, commands=commands)

    def getRank(self):
        return Rank(self._getNumber(0))

    def setRank(self, value):
        self._setNumber(0, value.value)

    def getDivision(self):
        return Division(self._getNumber(1))

    def setDivision(self, value):
        self._setNumber(1, value.value)

    def getScore(self):
        return self._getNumber(2)

    def setScore(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(PlatoonRankData, self)._initialize()
        self._addNumberProperty('rank')
        self._addNumberProperty('division')
        self._addNumberProperty('score', 0)