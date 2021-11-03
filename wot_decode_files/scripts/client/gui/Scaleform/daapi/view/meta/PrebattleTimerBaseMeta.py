# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PrebattleTimerBaseMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class PrebattleTimerBaseMeta(BaseDAAPIComponent):

    def as_setTimerS(self, totalTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimer(totalTime)

    def as_setMessageS(self, msg):
        if self._isDAAPIInited():
            return self.flashObject.as_setMessage(msg)

    def as_hideAllS(self, useAnim):
        if self._isDAAPIInited():
            return self.flashObject.as_hideAll(useAnim)

    def as_setWinConditionTextS(self, winCondition):
        if self._isDAAPIInited():
            return self.flashObject.as_setWinConditionText(winCondition)