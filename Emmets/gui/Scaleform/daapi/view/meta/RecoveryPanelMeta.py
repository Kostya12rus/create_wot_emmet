# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RecoveryPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RecoveryPanelMeta(BaseDAAPIComponent):

    def as_updateTimerS(self, time):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTimer(time)

    def as_displayHintS(self, display, animate):
        if self._isDAAPIInited():
            return self.flashObject.as_displayHint(display, animate)

    def as_displayCooldownS(self, display, animate):
        if self._isDAAPIInited():
            return self.flashObject.as_displayCooldown(display, animate)

    def as_setupTextsS(self, hint1, hint2, button):
        if self._isDAAPIInited():
            return self.flashObject.as_setupTexts(hint1, hint2, button)

    def as_updateTextsS(self, button):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTexts(button)