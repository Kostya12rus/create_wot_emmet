# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EpicBattlesAfterBattleViewMeta.py
from gui.Scaleform.framework.entities.View import View

class EpicBattlesAfterBattleViewMeta(View):

    def onIntroStartsPlaying(self):
        self._printOverrideError('onIntroStartsPlaying')

    def onRibbonStartsPlaying(self):
        self._printOverrideError('onRibbonStartsPlaying')

    def onNextBtnClick(self):
        self._printOverrideError('onNextBtnClick')

    def onCloseBtnClick(self):
        self._printOverrideError('onCloseBtnClick')

    def onRewardsBtnClick(self):
        self._printOverrideError('onRewardsBtnClick')

    def onEscapePress(self):
        self._printOverrideError('onEscapePress')

    def onProgressBarStartAnim(self):
        self._printOverrideError('onProgressBarStartAnim')

    def onProgressBarCompleteAnim(self):
        self._printOverrideError('onProgressBarCompleteAnim')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)