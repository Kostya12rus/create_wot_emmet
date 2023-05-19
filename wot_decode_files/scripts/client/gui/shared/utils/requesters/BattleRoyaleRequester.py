# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/BattleRoyaleRequester.py
import BigWorld
from adisp import adisp_async
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IBattleRoyaleRequester

class BattleRoyaleRequester(AbstractSyncDataRequester, IBattleRoyaleRequester):

    @property
    def accTitle(self):
        return self.getCacheValue('accBRTitle', (1, 0))

    @property
    def battleCount(self):
        return self.getCacheValue('BRBattlesCount', 0)

    @property
    def killCount(self):
        return self.getCacheValue('BRTotalKills', 0)

    @property
    def testDriveExpired(self):
        return self.getCacheValue('testDriveExpired', {})

    @property
    def topCount(self):
        return self.getCacheValue('BRSoloTop1Count') + self.getCacheValue('BRSquadTop1Count')

    def getStats(self, arenaBonusType, playerDatabaseID=None):
        if playerDatabaseID:
            return {}
        return self.getCacheValue('brBattleStats').get(arenaBonusType, {})

    @adisp_async
    def _requestCache(self, callback):
        BigWorld.player().battleRoyale.getCache((lambda resID, value: self._response(resID, value, callback)))

    def _preprocessValidData(self, data):
        if 'battleRoyale' in data:
            return dict(data['battleRoyale'])
        return dict()