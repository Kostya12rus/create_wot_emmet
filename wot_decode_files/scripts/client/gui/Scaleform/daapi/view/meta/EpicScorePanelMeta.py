# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EpicScorePanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EpicScorePanelMeta(BaseDAAPIComponent):

    def as_updateBasesS(self, west, center, east):
        if self._isDAAPIInited():
            return self.flashObject.as_updateBases(west, center, east)

    def as_updateHeadquarterHealthS(self, id, healthInPercent):
        if self._isDAAPIInited():
            return self.flashObject.as_updateHeadquarterHealth(id, healthInPercent)

    def as_headquarterDestroyedS(self, idx):
        if self._isDAAPIInited():
            return self.flashObject.as_headquarterDestroyed(idx)

    def as_updatePointsForBaseS(self, idx, points):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePointsForBase(idx, points)

    def as_setTargetS(self, targetType, targetId):
        if self._isDAAPIInited():
            return self.flashObject.as_setTarget(targetType, targetId)

    def as_setPrebattleTimerS(self, remainingPrebattleTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setPrebattleTimer(remainingPrebattleTime)