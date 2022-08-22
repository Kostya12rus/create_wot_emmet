# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleHintPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleHintPanelMeta(BaseDAAPIComponent):

    def onPlaySound(self, soundType):
        self._printOverrideError('onPlaySound')

    def onHideComplete(self):
        self._printOverrideError('onHideComplete')

    def as_setDataS(self, vKey, key, messageLeft, messageRight, offsetX, offsetY, reducedPanning):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(vKey, key, messageLeft, messageRight, offsetX, offsetY, reducedPanning)

    def as_toggleS(self, isShow):
        if self._isDAAPIInited():
            return self.flashObject.as_toggle(isShow)