# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/comp7/scheduler.py
from adisp import adisp_process
from gui import SystemMessages
from gui.impl import backport
from gui.impl.gen import R
from gui.periodic_battles.models import PrimeTimeStatus
from gui.prb_control import prbDispatcherProperty
from gui.prb_control.entities.base.ctx import LeavePrbAction
from gui.prb_control.entities.base.scheduler import BaseScheduler
from gui.prb_control.events_dispatcher import g_eventDispatcher
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

class Comp7Scheduler(BaseScheduler):
    comp7Controller = dependency.descriptor(IComp7Controller)

    def __init__(self, entity):
        super(Comp7Scheduler, self).__init__(entity)
        self.__isPrimeTime = False

    @prbDispatcherProperty
    def prbDispatcher(self):
        return

    def init(self):
        status, _, _ = self.comp7Controller.getPrimeTimeStatus()
        self.__isPrimeTime = status == PrimeTimeStatus.AVAILABLE
        self.comp7Controller.onStatusUpdated += self.__update

    def fini(self):
        self.comp7Controller.onStatusUpdated -= self.__update

    @adisp_process
    def __doLeave(self, isExit=True):
        yield self.prbDispatcher.doLeaveAction(LeavePrbAction(isExit))

    def __update(self, status):
        if not self.comp7Controller.isEnabled() or self.comp7Controller.isFrozen():
            self.__doLeave()
            return
        else:
            isPrimeTime = status == PrimeTimeStatus.AVAILABLE
            if isPrimeTime != self.__isPrimeTime:
                self.__isPrimeTime = isPrimeTime
                if self.comp7Controller.getCurrentCycleID() is not None:
                    if self.__isPrimeTime:
                        SystemMessages.pushMessage(text=backport.text(R.strings.comp7.system_messages.primeTime.start.body()), type=SystemMessages.SM_TYPE.PrimeTime, messageData={'title': backport.text(R.strings.comp7.system_messages.primeTime.start.title())})
                    else:
                        SystemMessages.pushMessage(text=backport.text(R.strings.comp7.system_messages.primeTime.end.body()), type=SystemMessages.SM_TYPE.PrimeTime, messageData={'title': backport.text(R.strings.comp7.system_messages.primeTime.end.title())})
                g_eventDispatcher.updateUI()
            return