# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CalendarMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CalendarMeta(BaseDAAPIComponent):

    def onMonthChanged(self, rawDate):
        self._printOverrideError('onMonthChanged')

    def onDateSelected(self, rawDate):
        self._printOverrideError('onDateSelected')

    def formatYMHeader(self, rawDate):
        self._printOverrideError('formatYMHeader')

    def as_openMonthS(self, rawDate):
        if self._isDAAPIInited():
            return self.flashObject.as_openMonth(rawDate)

    def as_selectDateS(self, rawDate):
        if self._isDAAPIInited():
            return self.flashObject.as_selectDate(rawDate)

    def as_setMinAvailableDateS(self, rawDate):
        if self._isDAAPIInited():
            return self.flashObject.as_setMinAvailableDate(rawDate)

    def as_setMaxAvailableDateS(self, rawDate):
        if self._isDAAPIInited():
            return self.flashObject.as_setMaxAvailableDate(rawDate)

    def as_setHighlightedDaysS(self, hightlightedTimestamps):
        if self._isDAAPIInited():
            return self.flashObject.as_setHighlightedDays(hightlightedTimestamps)

    def as_setDayTooltipTypeS(self, tooltipType):
        if self._isDAAPIInited():
            return self.flashObject.as_setDayTooltipType(tooltipType)