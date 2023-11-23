# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AnimatedBattleHintMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class AnimatedBattleHintMeta(BaseDAAPIComponent):

    def animFinish(self):
        self._printOverrideError('animFinish')

    def as_showHintS(self, frame, msgStr, isCompleted):
        if self._isDAAPIInited():
            return self.flashObject.as_showHint(frame, msgStr, isCompleted)

    def as_hideHintS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideHint()

    def as_closeHintS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_closeHint()

    def as_setPenetrationS(self, penetrationType, isPurple):
        if self._isDAAPIInited():
            return self.flashObject.as_setPenetration(penetrationType, isPurple)