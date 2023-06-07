# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SplashScreenMeta.py
from gui.Scaleform.daapi.view.meta.DAAPISimpleContainerMeta import DAAPISimpleContainerMeta

class SplashScreenMeta(DAAPISimpleContainerMeta):

    def onComplete(self):
        self._printOverrideError('onComplete')

    def onError(self):
        self._printOverrideError('onError')

    def fadeOutComplete(self):
        self._printOverrideError('fadeOutComplete')

    def as_playVideoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_playVideo(data)

    def as_setSizeS(self, width, height):
        if self._isDAAPIInited():
            return self.flashObject.as_setSize(width, height)

    def as_fadeOutS(self, time):
        if self._isDAAPIInited():
            return self.flashObject.as_fadeOut(time)