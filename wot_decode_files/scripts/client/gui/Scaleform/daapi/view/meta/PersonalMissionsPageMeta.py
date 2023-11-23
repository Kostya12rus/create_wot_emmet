# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PersonalMissionsPageMeta.py
from gui.Scaleform.framework.entities.View import View

class PersonalMissionsPageMeta(View):

    def onBarClick(self, chainID, operationIdx):
        self._printOverrideError('onBarClick')

    def onSkipTaskClick(self):
        self._printOverrideError('onSkipTaskClick')

    def onBackBtnClick(self):
        self._printOverrideError('onBackBtnClick')

    def closeView(self):
        self._printOverrideError('closeView')

    def onTutorialAcceptBtnClicked(self):
        self._printOverrideError('onTutorialAcceptBtnClicked')

    def showAwards(self):
        self._printOverrideError('showAwards')

    def as_setContentVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setContentVisible(value)

    def as_initViewS(self, pmType, chainsLen):
        if self._isDAAPIInited():
            return self.flashObject.as_initView(pmType, chainsLen)

    def as_reInitViewS(self, pmType, chainsLen):
        if self._isDAAPIInited():
            return self.flashObject.as_reInitView(pmType, chainsLen)

    def as_setHeaderDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderData(data)

    def as_updateSideBarDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSideBarData(data)

    def as_setStatusDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setStatusData(data)

    def as_setSelectedBranchIndexS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedBranchIndex(index)

    def as_showFirstAwardSheetObtainedPopupS(self, useAnim, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showFirstAwardSheetObtainedPopup(useAnim, data)

    def as_showFourAwardSheetsObtainedPopupS(self, useAnim, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showFourAwardSheetsObtainedPopup(useAnim, data)

    def as_hideAwardSheetObtainedPopupS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideAwardSheetObtainedPopup()

    def as_showAwardsPopoverForTutorS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showAwardsPopoverForTutor()