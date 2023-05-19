# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/comp7/tooltips/last_update_tooltip_model.py
from frameworks.wulf import ViewModel

class LastUpdateTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(LastUpdateTooltipModel, self).__init__(properties=properties, commands=commands)

    def getLeaderboardUpdateTimestamp(self):
        return self._getNumber(0)

    def setLeaderboardUpdateTimestamp(self, value):
        self._setNumber(0, value)

    def getDescription(self):
        return self._getString(1)

    def setDescription(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(LastUpdateTooltipModel, self)._initialize()
        self._addNumberProperty('leaderboardUpdateTimestamp', 0)
        self._addStringProperty('description', '')