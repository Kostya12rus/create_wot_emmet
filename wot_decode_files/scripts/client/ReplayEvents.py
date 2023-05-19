# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/ReplayEvents.py
import Event

class _ReplayEvents(object):

    @property
    def isPlaying(self):
        return self.__isPlaying

    @property
    def isRecording(self):
        return self.__isRecording

    def __init__(self):
        self.onTimeWarpStart = Event.Event()
        self.onTimeWarpFinish = Event.Event()
        self.onPause = Event.Event()
        self.onMuteSound = Event.Event()
        self.onWatcherNotify = Event.Event()
        self.onReplayTerminated = Event.Event()
        self.__isPlaying = False
        self.__isRecording = False

    def onRecording(self):
        self.__isRecording = True

    def onPlaying(self):
        self.__isPlaying = True


g_replayEvents = _ReplayEvents()