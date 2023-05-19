# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/tooltips/ranked/ranked_calendar_day_tooltip.py
from gui.impl.gen import R
from helpers import dependency
from gui.shared.tooltips import TOOLTIP_TYPE
from skeletons.gui.game_control import IRankedBattlesController
from gui.shared.tooltips.periodic.calendar_day import PeriodicCalendarDayTooltip

class RankedCalendarDayTooltip(PeriodicCalendarDayTooltip):
    _RES_ROOT = R.strings.ranked_battles.calendarDay
    _TOOLTIP_TYPE = TOOLTIP_TYPE.RANKED_CALENDAR_DAY
    __rankedController = dependency.descriptor(IRankedBattlesController)

    def _getController(self, *_):
        return self.__rankedController