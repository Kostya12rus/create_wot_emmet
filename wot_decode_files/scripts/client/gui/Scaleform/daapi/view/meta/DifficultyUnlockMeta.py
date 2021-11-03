# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/DifficultyUnlockMeta.py
from gui.Scaleform.framework.entities.View import View

class DifficultyUnlockMeta(View):

    def onCloseClick(self):
        self._printOverrideError('onCloseClick')

    def onDifficultyChangeClick(self):
        self._printOverrideError('onDifficultyChangeClick')

    def as_setDifficultyS(self, value, btnEnable=True):
        if self._isDAAPIInited():
            return self.flashObject.as_setDifficulty(value, btnEnable)

    def as_blurOtherWindowsS(self, layer):
        if self._isDAAPIInited():
            return self.flashObject.as_blurOtherWindows(layer)