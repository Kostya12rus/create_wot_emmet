# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/fun_random/tooltips/calendar_day_tooltip.py
from gui.impl.gen import R
from helpers import dependency
from gui.shared.tooltips import TOOLTIP_TYPE
from skeletons.gui.game_control import IFunRandomController
from gui.shared.tooltips.periodic.calendar_day import PeriodicCalendarDayTooltip

class FunRandomCalendarDayTooltip(PeriodicCalendarDayTooltip):
    _RES_ROOT = R.strings.fun_random.calendarDay
    _TOOLTIP_TYPE = TOOLTIP_TYPE.FUN_RANDOM_CALENDAR_DAY
    _controller = dependency.descriptor(IFunRandomController)