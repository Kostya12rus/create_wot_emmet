# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/view_events_listener.py
from debug_utils import LOG_UNEXPECTED
from gui.shared import EVENT_BUS_SCOPE
from gui.shared.events import ViewEventType
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.framework.managers.loaders import ViewLoadMode
from gui.Scaleform.framework.managers.containers import ChainItem

def _loadViewEventHandler(containerManager, e):
    containerManager.load(e.loadParams, *e.args, **e.kwargs)


def _loadGuiImplViewEventHandler(containerManager, e):
    containerManager.load(e.loadParams, *e.args, **e.kwargs)


def _preLoadViewEventHandler(containerManager, e):
    containerManager.load(SFViewLoadParams(e.alias, e.name, loadMode=ViewLoadMode.PRELOAD), e.ctx)


def _destroyViewEventHandler(containerManager, e):
    containerManager.destroyViews(e.alias, e.name)


def _destroyGuiImplViewEventHandler(containerManager, e):
    containerManager.destroyViews(e.alias)


def _loadViewsChainEventHandler(containerManager, e):
    items = [ ChainItem(event.loadParams, event.args, event.kwargs) for event in e.viewLoadEvents ]
    containerManager.loadChain(items)


_EVENT_HANDLERS = {ViewEventType.LOAD_VIEW: _loadViewEventHandler, 
   ViewEventType.LOAD_GUI_IMPL_VIEW: _loadGuiImplViewEventHandler, 
   ViewEventType.PRELOAD_VIEW: _preLoadViewEventHandler, 
   ViewEventType.DESTROY_VIEW: _destroyViewEventHandler, 
   ViewEventType.DESTROY_GUI_IMPL_VIEW: _destroyGuiImplViewEventHandler, 
   ViewEventType.LOAD_VIEWS_CHAIN: _loadViewsChainEventHandler}

class ViewEventsListener(EventSystemEntity):

    def __init__(self, appProxy):
        super(ViewEventsListener, self).__init__()
        self._app = appProxy
        self._waitingEvents = []

    def _populate(self):
        super(ViewEventsListener, self)._populate()
        self._addListeners()

    def _dispose(self):
        self._removeListeners()
        del self._waitingEvents[:]
        self._app = None
        super(ViewEventsListener, self)._dispose()
        return

    def handleWaitingEvents(self):
        if self._app.containerManager is not None:
            while self._waitingEvents:
                self._handleEvent(self._waitingEvents.pop(0))

        return

    def handleEvent(self, e):
        if self._app.containerManager is not None:
            self._handleEvent(e)
        else:
            self._waitingEvents.append(e)
        return

    def addWaitingEvent(self, e):
        self._waitingEvents.append(e)

    def _addListeners(self):
        for eventType in _EVENT_HANDLERS:
            if eventType != ViewEventType.LOAD_VIEW:
                for scope in EVENT_BUS_SCOPE.ALL:
                    self.addListener(eventType, self.handleEvent, scope=scope)

    def _removeListeners(self):
        for eventType in _EVENT_HANDLERS:
            if eventType != ViewEventType.LOAD_VIEW:
                for scope in EVENT_BUS_SCOPE.ALL:
                    self.removeListener(eventType, self.handleEvent, scope=scope)

    def _handleEvent(self, e):
        eventType = e.eventType
        if eventType in _EVENT_HANDLERS:
            handler = _EVENT_HANDLERS[eventType]
            handler(self._app.containerManager, e)
        else:
            LOG_UNEXPECTED('Unsupported event:', eventType, e)