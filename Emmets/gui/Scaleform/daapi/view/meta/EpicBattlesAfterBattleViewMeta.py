# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EpicBattlesAfterBattleViewMeta.py
from gui.Scaleform.framework.entities.View import View

class EpicBattlesAfterBattleViewMeta(View):

    def onIntroStartsPlaying(self):
        self._printOverrideError('onIntroStartsPlaying')

    def onRibbonStartsPlaying(self):
        self._printOverrideError('onRibbonStartsPlaying')

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