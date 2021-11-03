# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PrequeueWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class PrequeueWindowMeta(AbstractWindowView):

    def requestToEnqueue(self):
        self._printOverrideError('requestToEnqueue')

    def requestToLeave(self):
        self._printOverrideError('requestToLeave')

    def showFAQWindow(self):
        self._printOverrideError('showFAQWindow')

    def isEnqueueBtnEnabled(self):
        self._printOverrideError('isEnqueueBtnEnabled')

    def isLeaveBtnEnabled(self):
        self._printOverrideError('isLeaveBtnEnabled')

    def as_enableLeaveBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enableLeaveBtn(value)

    def as_enableEnqueueBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enableEnqueueBtn(value)