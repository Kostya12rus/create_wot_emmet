# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/battle_pass_requester.py
import BigWorld
from adisp import async
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester

class BattlePassRequester(AbstractSyncDataRequester):

    def getSeasonID(self):
        return self.getCacheValue('seasonID', 0)

    def getPoints(self):
        return self.getCacheValue('sumPoints', 0)

    def getCurrentLevel(self):
        return self.getCacheValue('level', 0)

    def getState(self):
        return self.getCacheValue('state', 0)

    def getPointsForVehicle(self, vehicleID, default=0):
        return self.getCacheValue('vehiclePoints', {}).get(vehicleID, default)

    def getPackedStats(self):
        return self.getCacheValue('packedStats', '')

    def getChosenItems(self):
        return self.getCacheValue('seasonStats', {}).get('chosenItems', {})

    def _preprocessValidData(self, data):
        return dict(data.get('battlePass', {}))

    @async
    def _requestCache(self, callback):
        BigWorld.player().battlePass.getCache(lambda resID, value: self._response(resID, value, callback))