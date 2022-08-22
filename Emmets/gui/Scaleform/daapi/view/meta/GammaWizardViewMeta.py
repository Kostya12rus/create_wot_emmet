# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/GammaWizardViewMeta.py
from gui.Scaleform.framework.entities.View import View

class GammaWizardViewMeta(View):

    def onClose(self):
        self._printOverrideError('onClose')

    def onApply(self):
        self._printOverrideError('onApply')

    def onChangeGamma(self, value):
        self._printOverrideError('onChangeGamma')

    def onReset(self):
        self._printOverrideError('onReset')

    def updateTexture(self, x, y, size):
        self._printOverrideError('updateTexture')

    def as_initDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_initData(data)