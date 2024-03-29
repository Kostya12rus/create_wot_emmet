# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/RankedRequester.py
import BigWorld
from adisp import adisp_async
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IRankedRequester

class RankedRequester(AbstractSyncDataRequester, IRankedRequester):

    @property
    def season(self):
        return self.getCacheValue('season', (-1, -1))

    @property
    def accRank(self):
        return self.getCacheValue('accRank', (0, 0))

    @property
    def maxRank(self):
        return self.getCacheValue('maxRank', (0, 0))

    @property
    def stepsCount(self):
        return self.getCacheValue('stepsCount', 0)

    @property
    def seasonStepsCount(self):
        return self.getCacheValue('seasonStepsCount', 0)

    @property
    def seasonEfficiencyStamp(self):
        return self.getCacheValue('currentEfficiency', {})

    @property
    def divisionsStats(self):
        return self.getCacheValue('divisions', {})

    @property
    def shields(self):
        return self.getCacheValue('shields', {})

    @property
    def persistentBonusBattles(self):
        return self.getCacheValue('bonusBattlesCount', 0)

    @property
    def dailyBonusBattles(self):
        return self.getCacheValue('dailyBonusBattlesCount', 0)

    @adisp_async
    def _requestCache(self, callback):
        BigWorld.player().ranked.getCache((lambda resID, value: self._response(resID, value, callback)))

    def _preprocessValidData(self, data):
        if 'ranked' in data:
            return dict(data['ranked'])
        return dict()