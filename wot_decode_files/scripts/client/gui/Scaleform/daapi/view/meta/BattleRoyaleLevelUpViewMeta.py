# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleRoyaleLevelUpViewMeta.py
from gui.Scaleform.framework.entities.View import View

class BattleRoyaleLevelUpViewMeta(View):

    def onIntroStartsPlaying(self):
        self._printOverrideError('onIntroStartsPlaying')

    def onRibbonStartsPlaying(self):
        self._printOverrideError('onRibbonStartsPlaying')

    def onCloseBtnClick(self):
        self._printOverrideError('onCloseBtnClick')

    def onEscapePress(self):
        self._printOverrideError('onEscapePress')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)