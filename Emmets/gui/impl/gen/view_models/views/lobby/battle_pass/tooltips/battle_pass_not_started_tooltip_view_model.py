# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/tooltips/battle_pass_not_started_tooltip_view_model.py
from frameworks.wulf import ViewModel

class BattlePassNotStartedTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BattlePassNotStartedTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getDate(self):
        return self._getString(0)

    def setDate(self, value):
        self._setString(0, value)

    def getSeasonNum(self):
        return self._getNumber(1)

    def setSeasonNum(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(BattlePassNotStartedTooltipViewModel, self)._initialize()
        self._addStringProperty('date', '')
        self._addNumberProperty('seasonNum', 0)