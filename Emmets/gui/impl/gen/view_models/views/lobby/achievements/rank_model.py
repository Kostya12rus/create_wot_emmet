# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/achievements/rank_model.py
from frameworks.wulf import ViewModel

class RankModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(RankModel, self).__init__(properties=properties, commands=commands)

    def getRank(self):
        return self._getNumber(0)

    def setRank(self, value):
        self._setNumber(0, value)

    def getSubRank(self):
        return self._getNumber(1)

    def setSubRank(self, value):
        self._setNumber(1, value)

    def getCountOfPoints(self):
        return self._getNumber(2)

    def setCountOfPoints(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(RankModel, self)._initialize()
        self._addNumberProperty('rank', 0)
        self._addNumberProperty('subRank', 0)
        self._addNumberProperty('countOfPoints', 0)