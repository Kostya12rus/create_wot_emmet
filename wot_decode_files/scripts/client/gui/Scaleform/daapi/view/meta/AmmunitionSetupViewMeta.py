# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AmmunitionSetupViewMeta.py
from gui.Scaleform.framework.entities.View import View

class AmmunitionSetupViewMeta(View):

    def onClose(self):
        self._printOverrideError('onClose')

    def onEscapePress(self):
        self._printOverrideError('onEscapePress')

    def as_gfSizeUpdatedS(self, x, width):
        if self._isDAAPIInited():
            return self.flashObject.as_gfSizeUpdated(x, width)

    def as_showCloseAnimS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showCloseAnim()

    def as_onAnimationEndS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_onAnimationEnd()

    def as_toggleParamsS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_toggleParams(isVisible)