# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/event/squad/scheduler.py
from adisp import process
from gui.prb_control import prbDispatcherProperty
from gui.prb_control.entities.base.ctx import PrbAction
from gui.prb_control.entities.event.pre_queue.scheduler import EventScheduler
from gui.prb_control.settings import PREBATTLE_ACTION_NAME

class EventSquadScheduler(EventScheduler):

    @prbDispatcherProperty
    def prbDispatcher(self):
        return

    def _doLeave(self):
        if self._entity.getFlags().isInQueue():
            if self._entity.getPlayerInfo().isCommander():
                self._entity.exitFromQueue()
        else:
            self._doSelect(PREBATTLE_ACTION_NAME.RANDOM)

    @process
    def _doSelect(self, actionName):
        yield self.prbDispatcher.doSelectAction(PrbAction(actionName))