# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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