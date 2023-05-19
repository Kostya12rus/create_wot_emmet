# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EpicDestroyTimersPanelMeta.py
from gui.Scaleform.daapi.view.battle.shared.timers_panel import TimersPanel

class EpicDestroyTimersPanelMeta(TimersPanel):

    def as_showAdditionalTimerS(self, timerTypeID, state):
        if self._isDAAPIInited():
            return self.flashObject.as_showAdditionalTimer(timerTypeID, state)

    def as_hideAdditionalTimerS(self, timerTypeID):
        if self._isDAAPIInited():
            return self.flashObject.as_hideAdditionalTimer(timerTypeID)

    def as_setAdditionalTimerStateS(self, timerTypeID, state):
        if self._isDAAPIInited():
            return self.flashObject.as_setAdditionalTimerState(timerTypeID, state)

    def as_setAdditionalTimerTimeStringS(self, timerTypeID, cooldownTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setAdditionalTimerTimeString(timerTypeID, cooldownTime)

    def as_setAdditionalTimerProgressValueS(self, timerTypeID, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setAdditionalTimerProgressValue(timerTypeID, progress)