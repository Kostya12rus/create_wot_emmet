# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/WaitingViewMeta.py
from gui.Scaleform.framework.entities.View import View

class WaitingViewMeta(View):

    def as_showWaitingS(self, message, softStart):
        if self._isDAAPIInited():
            return self.flashObject.as_showWaiting(message, softStart)

    def as_showBackgroundImgS(self, img, showSparks):
        if self._isDAAPIInited():
            return self.flashObject.as_showBackgroundImg(img, showSparks)

    def as_hideWaitingS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideWaiting()

    def as_showAwardsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showAwards(value)