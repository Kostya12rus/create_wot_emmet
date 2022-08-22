# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/battle_pass_requester.py
import BigWorld
from adisp import async
from battle_pass_common import BATTLE_PASS_PDATA_KEY
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IBattlePassRequester

class BattlePassRequester(AbstractSyncDataRequester, IBattlePassRequester):

    def getSeasonID(self):
        return self.getCacheValue('seasonID', 0)

    def getState(self):
        return self.getCacheValue('state', 0)

    def getActiveChapterID(self):
        return self.getCacheValue('chapterID', 0)

    def getPointsForVehicle(self, vehicleID, default=0):
        return self.getCacheValue('vehiclePoints', {}).get(vehicleID, default)

    def getPackedStats(self):
        return ''

    def getChapterStats(self):
        return self.getCacheValue('seasonStats', {}).get('chaptersStats', {})

    def getCurrentLevelByChapterID(self, chapterID):
        return self.getChapterStats().get(chapterID, {}).get('level', 0)

    def getPointsByChapterID(self, chapterID):
        return self.getChapterStats().get(chapterID, {}).get('points', 0)

    def getNonChapterPoints(self):
        return self.getCacheValue('seasonStats', {}).get('nonChapterPoints', 0)

    def _preprocessValidData(self, data):
        return dict(data.get(BATTLE_PASS_PDATA_KEY, {}))

    @async
    def _requestCache(self, callback):
        BigWorld.player().battlePass.getCache(lambda resID, value: self._response(resID, value, callback))