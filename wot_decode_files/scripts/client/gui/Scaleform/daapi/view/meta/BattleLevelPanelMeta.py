# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleLevelPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleLevelPanelMeta(BaseDAAPIComponent):

    def onPlaySound(self, soundType):
        self._printOverrideError('onPlaySound')

    def as_setLevelS(self, currentLevel, nextLevel, experience):
        if self._isDAAPIInited():
            return self.flashObject.as_setLevel(currentLevel, nextLevel, experience)

    def as_setExperienceS(self, currentExperience, targetExperience, expDiff, percent, playSound):
        if self._isDAAPIInited():
            return self.flashObject.as_setExperience(currentExperience, targetExperience, expDiff, percent, playSound)

    def as_setMaxLevelReachedS(self, levelReached):
        if self._isDAAPIInited():
            return self.flashObject.as_setMaxLevelReached(levelReached)

    def as_resetS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_reset()

    def as_setIsPausedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsPaused(value)

    def as_setAnimationS(self, enable):
        if self._isDAAPIInited():
            return self.flashObject.as_setAnimation(enable)