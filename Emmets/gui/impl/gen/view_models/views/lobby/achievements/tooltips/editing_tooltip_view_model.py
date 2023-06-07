# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/achievements/tooltips/editing_tooltip_view_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class TooltipType(Enum):
    DISABLED_LAYOUT = 'disabledLayout'
    NOT_ENOUGH_ACHIEVEMENTS = 'notEnoughAchievements'
    DISABLED = 'disabled'
    OTHER_PLAYER = 'otherPlayer'


class EditingTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(EditingTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getTooltipType(self):
        return TooltipType(self._getString(0))

    def setTooltipType(self, value):
        self._setString(0, value.value)

    def getRequiredAchievementsCount(self):
        return self._getNumber(1)

    def setRequiredAchievementsCount(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(EditingTooltipViewModel, self)._initialize()
        self._addStringProperty('tooltipType')
        self._addNumberProperty('requiredAchievementsCount', 0)