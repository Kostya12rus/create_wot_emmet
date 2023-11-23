# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCIntroVideoPageMeta.py
from gui.Scaleform.framework.entities.View import View

class BCIntroVideoPageMeta(View):

    def videoStarted(self):
        self._printOverrideError('videoStarted')

    def videoFinished(self):
        self._printOverrideError('videoFinished')

    def goToBattle(self):
        self._printOverrideError('goToBattle')

    def skipBootcamp(self):
        self._printOverrideError('skipBootcamp')

    def handleError(self, data):
        self._printOverrideError('handleError')

    def onHighlightShow(self):
        self._printOverrideError('onHighlightShow')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_updateProgressS(self, percent):
        if self._isDAAPIInited():
            return self.flashObject.as_updateProgress(percent)

    def as_loadedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_loaded()

    def as_showIntroPageS(self, value, showRewards=False):
        if self._isDAAPIInited():
            return self.flashObject.as_showIntroPage(value, showRewards)

    def as_pausePlaybackS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_pausePlayback()

    def as_resumePlaybackS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_resumePlayback()