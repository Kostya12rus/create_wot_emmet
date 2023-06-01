# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/achievements/tooltips/wtr_main_tooltip_view_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.achievements.rank_model import RankModel

class WtrMainTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(WtrMainTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getRequiredNumberOfBattles(self):
        return self._getNumber(0)

    def setRequiredNumberOfBattles(self, value):
        self._setNumber(0, value)

    def getCurrentPoints(self):
        return self._getNumber(1)

    def setCurrentPoints(self, value):
        self._setNumber(1, value)

    def getRank(self):
        return self._getNumber(2)

    def setRank(self, value):
        self._setNumber(2, value)

    def getSubRank(self):
        return self._getNumber(3)

    def setSubRank(self, value):
        self._setNumber(3, value)

    def getRanks(self):
        return self._getArray(4)

    def setRanks(self, value):
        self._setArray(4, value)

    @staticmethod
    def getRanksType():
        return RankModel

    def _initialize(self):
        super(WtrMainTooltipViewModel, self)._initialize()
        self._addNumberProperty('requiredNumberOfBattles', 0)
        self._addNumberProperty('currentPoints', 0)
        self._addNumberProperty('rank', 0)
        self._addNumberProperty('subRank', 0)
        self._addArrayProperty('ranks', Array())