# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PersonalMissionFirstEntryViewMeta.py
from gui.Scaleform.framework.entities.View import View

class PersonalMissionFirstEntryViewMeta(View):

    def playVideo(self):
        self._printOverrideError('playVideo')

    def backBtnClicked(self):
        self._printOverrideError('backBtnClicked')

    def onViewClose(self, isAcceptBtnClick):
        self._printOverrideError('onViewClose')

    def onCardClick(self, cardID):
        self._printOverrideError('onCardClick')

    def onNextCardClick(self, cardID):
        self._printOverrideError('onNextCardClick')

    def onPrevCardClick(self, cardID):
        self._printOverrideError('onPrevCardClick')

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setDetailedCardDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setDetailedCardData(data)