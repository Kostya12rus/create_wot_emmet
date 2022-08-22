# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/dog_tags/ranked_season_efficiency_model.py
from frameworks.wulf import ViewModel

class RankedSeasonEfficiencyModel(ViewModel):
    __slots__ = ()
    PERIOD_PAST = 0
    PERIOD_CURRENT = 1
    PERIOD_FUTURE = 2
    EFFICIENCY_DEFAULT = 0
    EFFICIENCY_BEST = 1
    EFFICIENCY_OUT_OF_LEAGUE = 2
    WAITING_AWARDS = 3

    def __init__(self, properties=3, commands=0):
        super(RankedSeasonEfficiencyModel, self).__init__(properties=properties, commands=commands)

    def getValue(self):
        return self._getReal(0)

    def setValue(self, value):
        self._setReal(0, value)

    def getPeriodState(self):
        return self._getNumber(1)

    def setPeriodState(self, value):
        self._setNumber(1, value)

    def getEfficiencyState(self):
        return self._getNumber(2)

    def setEfficiencyState(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(RankedSeasonEfficiencyModel, self)._initialize()
        self._addRealProperty('value', 0.0)
        self._addNumberProperty('periodState', 0)
        self._addNumberProperty('efficiencyState', 0)