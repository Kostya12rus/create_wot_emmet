# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EpicInGameRankMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EpicInGameRankMeta(BaseDAAPIComponent):

    def levelUpAnimationComplete(self):
        self._printOverrideError('levelUpAnimationComplete')

    def as_triggerLevelUpS(self, previousProgress):
        if self._isDAAPIInited():
            return self.flashObject.as_triggerLevelUp(previousProgress)

    def as_updateProgressS(self, previousProgress, currentProgress):
        if self._isDAAPIInited():
            return self.flashObject.as_updateProgress(previousProgress, currentProgress)

    def as_setRankS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setRank(data)