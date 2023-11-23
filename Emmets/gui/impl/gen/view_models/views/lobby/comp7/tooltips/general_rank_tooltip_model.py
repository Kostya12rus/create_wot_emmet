# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/comp7/tooltips/general_rank_tooltip_model.py
from enum import IntEnum
from frameworks.wulf import ViewModel

class Rank(IntEnum):
    FIRST = 6
    SECOND = 5
    THIRD = 4
    FOURTH = 3
    FIFTH = 2
    SIXTH = 1


class GeneralRankTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(GeneralRankTooltipModel, self).__init__(properties=properties, commands=commands)

    def getRank(self):
        return Rank(self._getNumber(0))

    def setRank(self, value):
        self._setNumber(0, value.value)

    def getDivisions(self):
        return self._getString(1)

    def setDivisions(self, value):
        self._setString(1, value)

    def getFrom(self):
        return self._getNumber(2)

    def setFrom(self, value):
        self._setNumber(2, value)

    def getTo(self):
        return self._getNumber(3)

    def setTo(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(GeneralRankTooltipModel, self)._initialize()
        self._addNumberProperty('rank')
        self._addStringProperty('divisions', 'E, D, C, B, A')
        self._addNumberProperty('from', 1000)
        self._addNumberProperty('to', 2000)