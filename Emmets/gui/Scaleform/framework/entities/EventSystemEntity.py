# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/EventSystemEntity.py
from gui.Scaleform.framework.entities.DisposableEntity import DisposableEntity
from gui.shared import g_eventBus, EVENT_BUS_SCOPE, EventPriority

class EventSystemEntity(DisposableEntity):

    def fireEvent(self, event, scope=EVENT_BUS_SCOPE.DEFAULT):
        g_eventBus.handleEvent(event, scope=scope)

    def addListener(self, eventType, handler, scope=EVENT_BUS_SCOPE.DEFAULT, priority=EventPriority.DEFAULT):
        g_eventBus.addListener(eventType, handler, scope=scope, priority=priority)

    def removeListener(self, eventType, handler, scope=EVENT_BUS_SCOPE.DEFAULT):
        g_eventBus.removeListener(eventType, handler, scope)

    def addRestriction(self, eventType, restriction, scope=EVENT_BUS_SCOPE.DEFAULT, priority=EventPriority.DEFAULT):
        g_eventBus.addRestriction(eventType, restriction, scope=scope, priority=priority)

    def removeRestriction(self, eventType, restriction, scope=EVENT_BUS_SCOPE.DEFAULT):
        g_eventBus.removeRestriction(eventType, restriction, scope)