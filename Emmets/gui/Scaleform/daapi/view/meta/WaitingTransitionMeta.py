# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/WaitingTransitionMeta.py
from gui.Scaleform.daapi.view.meta.DAAPISimpleContainerMeta import DAAPISimpleContainerMeta

class WaitingTransitionMeta(DAAPISimpleContainerMeta):

    def as_setTransitionTextS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setTransitionText(text)

    def as_updateStageS(self, width, height, scale):
        if self._isDAAPIInited():
            return self.flashObject.as_updateStage(width, height, scale)

    def as_showBGS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showBG()

    def as_hideBGS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideBG()