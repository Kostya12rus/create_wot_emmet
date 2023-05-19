# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCTooltipsWindowMeta.py
from gui.Scaleform.framework.entities.View import View

class BCTooltipsWindowMeta(View):

    def animFinish(self):
        self._printOverrideError('animFinish')

    def as_setRotateTipVisibilityS(self, Visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setRotateTipVisibility(Visible)

    def as_showHandlerS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showHandler()

    def as_completeHandlerS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_completeHandler()

    def as_hideHandlerS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideHandler()