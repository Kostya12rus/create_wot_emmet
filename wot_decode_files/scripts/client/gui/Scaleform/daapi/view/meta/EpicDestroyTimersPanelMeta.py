# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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