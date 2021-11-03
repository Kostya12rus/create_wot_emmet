# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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