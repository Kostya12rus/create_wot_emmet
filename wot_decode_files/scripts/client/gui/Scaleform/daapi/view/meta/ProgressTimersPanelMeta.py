# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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