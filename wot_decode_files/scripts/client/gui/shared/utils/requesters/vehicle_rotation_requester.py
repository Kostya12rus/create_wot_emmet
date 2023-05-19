# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/vehicle_rotation_requester.py
import BigWorld
from adisp import adisp_async
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IVehicleRotationRequester

class VehicleRotationRequester(AbstractSyncDataRequester, IVehicleRotationRequester):

    def getBattlesCount(self, groupNum):
        battlesCount = self._groupLocks['groupBattles']
        groupIdx = max(0, groupNum - 1)
        if len(battlesCount) > groupIdx:
            return battlesCount[groupIdx]
        return -1

    def isGroupLocked(self, groupNum):
        if groupNum == 0:
            return False
        groupsLocks = self._groupLocks['isGroupLocked']
        groupIdx = max(0, groupNum - 1)
        if len(groupsLocks) > groupIdx:
            return groupsLocks[groupIdx]
        return False

    def getGroupNum(self, vehIntCD):
        return self.getCacheValue('vehiclesGroupMapping', {}).get(vehIntCD, 0)

    def isInfinite(self, groupNum):
        return self.getBattlesCount(groupNum) == -1

    def unlockedBy(self, groupNum):
        playGroupsToUnlock = self._groupLocks['unlockedBy']
        return playGroupsToUnlock.get(groupNum, -1)

    @property
    def _groupLocks(self):
        return self.getCacheValue('groupLocks', {'groupBattles': [], 'isGroupLocked': [], 'unlockedBy': {}})

    @adisp_async
    def _requestCache(self, callback):
        BigWorld.player().vehicleRotation.getCache((lambda resID, value: self._response(resID, value, callback)))