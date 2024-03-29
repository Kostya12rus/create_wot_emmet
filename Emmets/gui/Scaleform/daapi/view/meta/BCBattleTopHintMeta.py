# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCBattleTopHintMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BCBattleTopHintMeta(BaseDAAPIComponent):

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