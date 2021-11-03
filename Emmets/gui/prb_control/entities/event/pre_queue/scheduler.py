# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/event/pre_queue/scheduler.py
from adisp import process
from gui.prb_control.entities.base.scheduler import BaseScheduler
from helpers import dependency
from skeletons.gui.server_events import IEventsCache
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.prb_control.entities.base.ctx import LeavePrbAction
from gui.prb_control import prbDispatcherProperty

class EventScheduler(BaseScheduler):
    _eventsCache = dependency.descriptor(IEventsCache)

    @prbDispatcherProperty
    def prbDispatcher(self):
        return

    def init(self):
        self._eventsCache.onSyncCompleted += self._onSyncCompleted

    def fini(self):
        self._eventsCache.onSyncCompleted -= self._onSyncCompleted

    def _onSyncCompleted(self, *_):
        if not self._eventsCache.isEventEnabled():
            self._doLeave()
            self._hideTopWindows()

    @process
    def _doLeave(self, isExit=True):
        if self.prbDispatcher:
            yield self.prbDispatcher.doLeaveAction(LeavePrbAction(isExit))

    @process
    def _hideTopWindows(self):
        from gui.shared import event_dispatcher
        yield event_dispatcher.hideTopWindows()
        g_eventDispatcher.loadHangar()