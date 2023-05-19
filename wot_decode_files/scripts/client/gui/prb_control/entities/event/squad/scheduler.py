# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/event/squad/scheduler.py
from adisp import adisp_process
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

    @adisp_process
    def _doSelect(self, actionName):
        yield self.prbDispatcher.doSelectAction(PrbAction(actionName))