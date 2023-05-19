# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BrowserViewStackExPaddingMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BrowserViewStackExPaddingMeta(BaseDAAPIComponent):

    def setViewSize(self, width, height):
        self._printOverrideError('setViewSize')

    def as_setAllowWaitingS(self, value, startImmediately):
        if self._isDAAPIInited():
            return self.flashObject.as_setAllowWaiting(value, startImmediately)

    def as_setWaitingMessageS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setWaitingMessage(value)

    def as_createBrowserViewS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_createBrowserView()