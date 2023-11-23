# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesRewardsRanksMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RankedBattlesRewardsRanksMeta(BaseDAAPIComponent):

    def onRequestData(self, index, iconSizeID, rewardsCount):
        self._printOverrideError('onRequestData')

    def as_setDivisionsDataS(self, divisions, immediately):
        if self._isDAAPIInited():
            return self.flashObject.as_setDivisionsData(divisions, immediately)

    def as_setRewardsS(self, rewards, isQualification):
        if self._isDAAPIInited():
            return self.flashObject.as_setRewards(rewards, isQualification)