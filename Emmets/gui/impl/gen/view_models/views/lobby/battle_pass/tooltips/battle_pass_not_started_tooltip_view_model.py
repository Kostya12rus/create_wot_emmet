# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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