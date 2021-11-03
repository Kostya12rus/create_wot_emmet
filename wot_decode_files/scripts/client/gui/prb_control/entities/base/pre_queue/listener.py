# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/base/pre_queue/listener.py
from gui.prb_control.entities.base.listener import IPrbListener

class IPreQueueListener(IPrbListener):

    def onEnqueued(self, queueType, *args):
        pass

    def onDequeued(self, queueType, *args):
        pass

    def onEnqueueError(self, queueType, *args):
        pass

    def onKickedFromQueue(self, queueType, *args):
        pass

    def onKickedFromArena(self, queueType, *args):
        pass

    def onArenaJoinFailure(self, queueType, *args):
        pass

    def onPreQueueSettingsChanged(self, diff):
        pass