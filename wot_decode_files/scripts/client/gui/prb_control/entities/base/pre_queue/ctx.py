# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/base/pre_queue/ctx.py
from gui.prb_control.entities.base.ctx import PrbCtrlRequestCtx
from gui.prb_control.settings import CTRL_ENTITY_TYPE, REQUEST_TYPE
from gui.prb_control.settings import FUNCTIONAL_FLAG
from gui.shared.utils.decorators import ReprInjector

class _PreQueueRequestCtx(PrbCtrlRequestCtx):

    def __init__(self, **kwargs):
        super(_PreQueueRequestCtx, self).__init__(ctrlType=CTRL_ENTITY_TYPE.PREQUEUE, **kwargs)


class QueueCtx(_PreQueueRequestCtx):

    def getRequestType(self):
        return REQUEST_TYPE.QUEUE


class DequeueCtx(_PreQueueRequestCtx):

    def getRequestType(self):
        return REQUEST_TYPE.DEQUEUE


class JoinPreQueueModeCtx(_PreQueueRequestCtx):

    def __init__(self, queueType, flags=FUNCTIONAL_FLAG.UNDEFINED, waitingID=''):
        super(JoinPreQueueModeCtx, self).__init__(entityType=queueType, flags=flags, waitingID=waitingID)

    def getID(self):
        return 0


@ReprInjector.withParent(('getWaitingID', 'waitingID'))
class LeavePreQueueCtx(_PreQueueRequestCtx):

    def getRequestType(self):
        return REQUEST_TYPE.LEAVE