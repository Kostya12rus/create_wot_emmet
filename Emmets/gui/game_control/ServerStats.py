# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_control/ServerStats.py
import BigWorld, Event, constants
from PlayerEvents import g_playerEvents
from gui.Scaleform.locale.MENU import MENU
from gui.impl import backport
from gui.shared.formatters import text_styles
from skeletons.gui.game_control import IServerStatsController
_STATS_REQUEST_TIMEOUT = 5.0

class STATS_TYPE(object):
    UNAVAILABLE = 'unavailable'
    CLUSTER = 'clusterCCU'
    FULL = 'regionCCU/clusterCCU'


class ServerStats(IServerStatsController):

    def __init__(self):
        super(ServerStats, self).__init__()
        self.__statsCallbackID = None
        self.__stats = {}
        self.onStatsReceived = Event.Event()
        return

    def onLobbyStarted(self, ctx):
        g_playerEvents.onServerStatsReceived += self.__onStatsReceived
        self.__loadStatsCallback(0.0)

    def onAvatarBecomePlayer(self):
        self.__stop()

    def onDisconnected(self):
        self.__stop()

    def getFormattedStats(self):
        clusterUsers, regionUsers, tooltipType = self.getStats()
        if tooltipType == STATS_TYPE.CLUSTER:
            statsStr = text_styles.stats(clusterUsers)
        elif tooltipType == STATS_TYPE.UNAVAILABLE:
            statsStr = text_styles.main(MENU.ONLINECOUNTER_UNAVAILABLE)
        else:
            statsStr = text_styles.concatStylesToSingleLine(text_styles.stats(clusterUsers), text_styles.main(MENU.ONLINECOUNTER_DELIMITER), text_styles.main(regionUsers))
        return (
         statsStr, tooltipType)

    def getStats(self):
        clusterCCU = self.__stats.get('clusterCCU', 0)
        regionCCU = self.__stats.get('regionCCU', 0)
        if regionCCU and not constants.IS_CHINA:
            clusterUsers = backport.getIntegralFormat(clusterCCU)
            regionUsers = backport.getIntegralFormat(regionCCU)
            if clusterCCU == regionCCU:
                tooltipType = STATS_TYPE.CLUSTER
            else:
                tooltipType = STATS_TYPE.FULL
        else:
            clusterUsers = regionUsers = '-'
            tooltipType = STATS_TYPE.UNAVAILABLE
        return (clusterUsers, regionUsers, tooltipType)

    def __stop(self):
        g_playerEvents.onServerStatsReceived -= self.__onStatsReceived
        self.__clearStatsCallback()

    def __onStatsReceived(self, stats):
        self.__stats = dict(stats)
        self.onStatsReceived()
        self.__loadStatsCallback()

    def __requestServerStats(self):
        self.__clearStatsCallback()
        if hasattr(BigWorld.player(), 'requestServerStats'):
            BigWorld.player().requestServerStats()

    def __loadStatsCallback(self, timeout=None):
        if constants.IS_SHOW_SERVER_STATS:
            self.__statsCallbackID = BigWorld.callback(timeout if timeout is not None else _STATS_REQUEST_TIMEOUT, self.__requestServerStats)
        return

    def __clearStatsCallback(self):
        if self.__statsCallbackID is not None:
            BigWorld.cancelCallback(self.__statsCallbackID)
            self.__statsCallbackID = None
        return