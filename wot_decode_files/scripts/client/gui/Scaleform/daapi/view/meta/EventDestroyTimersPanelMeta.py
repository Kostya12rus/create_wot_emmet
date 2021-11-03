# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EventDestroyTimersPanelMeta.py
from gui.Scaleform.daapi.view.battle.shared.timers_panel import TimersPanel

class EventDestroyTimersPanelMeta(TimersPanel):

    def setComponentsOverlay(self, isRibbonsPanelOverlay, isBuffsPanelOverlay):
        self._printOverrideError('setComponentsOverlay')

    def as_setWarningTextS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setWarningText(text)

    def as_setFillingInProgressS(self, current, total, isActive, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setFillingInProgress(current, total, isActive, visible)

    def as_setGotoPointTimerS(self, timeLeft, timeMax, message, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setGotoPointTimer(timeLeft, timeMax, message, visible)

    def as_setWaitForAlliesS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setWaitForAllies(visible)

    def as_hideAllNotificationsS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideAllNotifications()