# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/components/CalendarComponent.py
from Event import Event, EventManager
from gui.Scaleform.daapi.view.meta.CalendarMeta import CalendarMeta
from gui.impl import backport

class CalendarComponent(CalendarMeta):

    def __init__(self):
        super(CalendarComponent, self).__init__()
        self.__em = EventManager()
        self.onMonthChangedEvent = Event(self.__em)
        self.onDateSelectedEvent = Event(self.__em)

    def onMonthChanged(self, timestamp):
        self.onMonthChangedEvent(timestamp)

    def onDateSelected(self, timestamp):
        self.onDateSelectedEvent(timestamp)

    def formatYMHeader(self, rawDate):
        return backport.getYearMonthFormat(rawDate)

    def _dispose(self):
        self.__em.clear()
        super(CalendarComponent, self)._dispose()