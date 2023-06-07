# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/achievements20_requester.py
import typing, BigWorld
from adisp import adisp_async
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IAchievements20Requester
from constants import AchievementsLayoutStates
if typing.TYPE_CHECKING:
    from typing import List

class Achievements20Requester(AbstractSyncDataRequester, IAchievements20Requester):

    def getLayout(self):
        return self.getCacheValue('achievementsLayout', {}).get('layout', [])

    def getLayoutState(self):
        return self.getCacheValue('achievementsLayout', {}).get('state', AchievementsLayoutStates.AUTO)

    def getAchievementBitmask(self):
        return self.getCacheValue('achievementsLayout', {}).get('achievementBitmask', AchievementsLayoutStates.AUTO)

    def getLayoutLength(self):
        return self.getCacheValue('achievementsLayout', {}).get('layoutLength', 0)

    def _preprocessValidData(self, data):
        return dict(data.get('achievements20', {}))

    @adisp_async
    def _requestCache(self, callback):
        BigWorld.player().achievements20.getCache((lambda resID, value: self._response(resID, value, callback)))