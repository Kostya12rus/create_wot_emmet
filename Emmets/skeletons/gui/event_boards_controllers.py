# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/event_boards_controllers.py
from adisp import adisp_process, adisp_async

class IEventBoardController(object):

    def getPlayerEventsData(self):
        raise NotImplementedError

    def hasEvents(self):
        raise NotImplementedError

    def getEventsSettingsData(self):
        raise NotImplementedError

    def getMyEventsTopData(self):
        raise NotImplementedError

    def getHangarFlagData(self):
        raise NotImplementedError

    def updateHangarFlag(self):
        raise NotImplementedError

    def cleanEventsData(self):
        raise NotImplementedError

    @adisp_async
    @adisp_process
    def joinEvent(self, eventID, callback):
        raise NotImplementedError

    @adisp_async
    @adisp_process
    def leaveEvent(self, eventID, callback):
        raise NotImplementedError

    @adisp_async
    @adisp_process
    def getHangarFlag(self, callback, onLogin=False):
        raise NotImplementedError

    @adisp_async
    @adisp_process
    def getEvents(self, callback, onlySettings=True, isTabVisited=False, onLogin=False, prefetchKeyArtBig=True):
        raise NotImplementedError

    @adisp_async
    @adisp_process
    def getMyLeaderboardInfo(self, eventID, leaderboardID, callback, showNotification=True):
        raise NotImplementedError

    @adisp_async
    @adisp_process
    def getLeaderboard(self, eventID, leaderboardID, pageNumber, callback, leaderBoardClass=None, showNotification=True):
        raise NotImplementedError