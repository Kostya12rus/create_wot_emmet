# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EpicBattlesWelcomeBackViewMeta.py
from gui.Scaleform.framework.entities.View import View

class EpicBattlesWelcomeBackViewMeta(View):

    def onBackBtnClicked(self):
        self._printOverrideError('onBackBtnClicked')

    def onCloseBtnClicked(self):
        self._printOverrideError('onCloseBtnClicked')

    def onContinueBtnClicked(self):
        self._printOverrideError('onContinueBtnClicked')

    def onChangesLinkClicked(self):
        self._printOverrideError('onChangesLinkClicked')

    def playVideo(self):
        self._printOverrideError('playVideo')

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)