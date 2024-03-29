# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/entity_events.py
from Event import Event, SafeEvent, EventManager, ContextEvent, SafeComponentEvent
from synchronous_event import SynchronousEvent
from events_debugger import EventsDebugger

class EntityEvents(object):
    __slots__ = ('_eventManager', '_debugger')

    def __init__(self):
        self._eventManager = EventManager()
        self._debugger = None
        return

    def _createEvent(self):
        return SafeEvent(self._eventManager)

    def _createSynchronousEvent(self):
        return SynchronousEvent(self._eventManager)

    def _createUnsafeEvent(self):
        return Event(self._eventManager)

    def _createContextEvent(self):
        return ContextEvent(self._eventManager)

    def createComponentEvent(self, component):
        return SafeComponentEvent(self._eventManager, component)

    def clear(self):
        self._eventManager.clear()

    def destroy(self):
        self.clear()

    def debugEvents(self):
        self._debugger = EventsDebugger(self)