# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCMessageWindowMeta.py
from tutorial.gui.Scaleform.pop_ups import TutorialDialog

class BCMessageWindowMeta(TutorialDialog):

    def onMessageRemoved(self):
        self._printOverrideError('onMessageRemoved')

    def onMessageAppear(self, rendrerer):
        self._printOverrideError('onMessageAppear')

    def onMessageDisappear(self, rendrerer, animation):
        self._printOverrideError('onMessageDisappear')

    def onMessageExecuted(self, rendrerer):
        self._printOverrideError('onMessageExecuted')

    def onMessageButtonClicked(self):
        self._printOverrideError('onMessageButtonClicked')

    def onMessageAnimationStopped(self, animation):
        self._printOverrideError('onMessageAnimationStopped')

    def onMessageAnimationStarted(self, animation):
        self._printOverrideError('onMessageAnimationStarted')

    def hideBlur(self):
        self._printOverrideError('hideBlur')

    def as_setMessageDataS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setMessageData(value)

    def as_blurOtherWindowsS(self, layer):
        if self._isDAAPIInited():
            return self.flashObject.as_blurOtherWindows(layer)