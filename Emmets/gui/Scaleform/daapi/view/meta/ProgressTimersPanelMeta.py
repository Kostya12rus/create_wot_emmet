# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProgressTimersPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ProgressTimersPanelMeta(BaseDAAPIComponent):

    def as_setLocalizedDataS(self, type, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setLocalizedData(type, data)

    def as_showS(self, timerTypeID, state, id):
        if self._isDAAPIInited():
            return self.flashObject.as_show(timerTypeID, state, id)

    def as_hideS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide()

    def as_setStateS(self, state):
        if self._isDAAPIInited():
            return self.flashObject.as_setState(state)

    def as_setTimeStringS(self, cooldownTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimeString(cooldownTime)

    def as_setProgressValueS(self, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgressValue(progress)