# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/comp7/tooltips/comp7_calendar_day_tooltip.py
from gui.impl.gen import R
from gui.shared.tooltips import TOOLTIP_TYPE
from gui.shared.tooltips.periodic.calendar_day import PeriodicCalendarDayTooltip
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

class Comp7CalendarDayTooltip(PeriodicCalendarDayTooltip):
    _controller = dependency.descriptor(IComp7Controller)
    _TOOLTIP_TYPE = TOOLTIP_TYPE.COMP7_CALENDAR_DAY_INFO
    _RES_ROOT = R.strings.comp7.calendarDay

    def _getController(self, *_):
        return self._controller