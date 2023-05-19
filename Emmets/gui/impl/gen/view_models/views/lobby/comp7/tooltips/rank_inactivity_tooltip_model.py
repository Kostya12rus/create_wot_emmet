# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/comp7/tooltips/rank_inactivity_tooltip_model.py
from frameworks.wulf import ViewModel

class RankInactivityTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(RankInactivityTooltipModel, self).__init__(properties=properties, commands=commands)

    def getRankInactivityCount(self):
        return self._getNumber(0)

    def setRankInactivityCount(self, value):
        self._setNumber(0, value)

    def _initialize(self):
        super(RankInactivityTooltipModel, self)._initialize()
        self._addNumberProperty('rankInactivityCount', -1)