# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/calendar.py
from gui.game_control import CalendarInvokeOrigin
from helpers import dependency
from skeletons.gui.game_control import ICalendarController
from web.web_client_api import w2c, W2CSchema, Field

def _invokedFromValidator(value, _):
    return not value or value in CalendarInvokeOrigin.ALL()


class _OpenCalendarSchema(W2CSchema):
    url = Field(required=False, type=basestring)
    invoked_from = Field(required=False, type=basestring, validator=_invokedFromValidator)


class OpenCalendarWindowWebApiMixin(object):
    __calendarController = dependency.descriptor(ICalendarController)

    @w2c(_OpenCalendarSchema, 'calendar')
    def openCalendar(self, cmd):
        self.__calendarController.showWindow(cmd.url, cmd.invoked_from)