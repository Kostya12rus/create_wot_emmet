# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EventTimerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EventTimerMeta(BaseDAAPIComponent):

    def as_updateTimeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTime(value)

    def as_setTimerStateS(self, state):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimerState(state)

    def as_playFxS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_playFx()

    def as_updateTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTitle(value)

    def as_updateProgressBarS(self, value, vis):
        if self._isDAAPIInited():
            return self.flashObject.as_updateProgressBar(value, vis)