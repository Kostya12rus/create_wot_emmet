# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/helpers/statistics.py


class IStatisticsCollector(object):

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    @property
    def update(self):
        raise NotImplementedError

    def needCollectSystemData(self, value):
        raise NotImplementedError

    def needCollectSessionData(self, value):
        raise NotImplementedError

    def getStatistics(self, andStop=True):
        raise NotImplementedError

    def getSessionData(self):
        raise NotImplementedError

    def noteHangarLoadingState(self, state, initialState=False, showSummaryNow=False):
        raise NotImplementedError

    def noteLastArenaData(self, arenaTypeID, arenaUniqueID, arenaTeam, randomEvents):
        raise NotImplementedError