# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/platform/base/statuses/events_mgr.py
import typing, Event
from gui.platform.base.logger import getWithContext
from gui.platform.base.statuses.constants import StatusTypes, DEFAULT_CONTEXT
if typing.TYPE_CHECKING:
    from gui.platform.base.statuses.status import Status

class StatusEventsManager(object):

    def __init__(self):
        self._logger = getWithContext(instance=self)
        self._em = Event.EventManager()
        self._events = {}

    def subscribe(self, statusType, handler, context=DEFAULT_CONTEXT):
        events = self._events.setdefault(context, {})
        if statusType not in events:
            events[statusType] = Event.SafeEvent(self._em)
        events[statusType] += handler
        self._logger.debug('Subscribed to (%s|%s|%s).', context, statusType, handler)

    def unsubscribe(self, statusType, handler, context=DEFAULT_CONTEXT):
        event = self._get(context, statusType)
        if event:
            event -= handler
            self._logger.debug('Unsubscribed from (%s|%s|%s).', context, statusType, handler)

    def send(self, status, context=DEFAULT_CONTEXT):
        event = self._get(context, status.type)
        if event:
            self._logger.debug('Sending %s for (%s|%s).', status, context, event)
            event(status)

    def clear(self):
        self._em.clear()
        self._events.clear()
        self._logger.debug('All events cleared.')

    def _get(self, context, statusType):
        return self._events.get(context, {}).get(statusType)