# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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