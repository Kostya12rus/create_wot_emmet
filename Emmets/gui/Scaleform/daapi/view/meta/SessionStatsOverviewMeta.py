# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SessionStatsOverviewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class SessionStatsOverviewMeta(BaseDAAPIComponent):

    def onClickMoreBtn(self):
        self._printOverrideError('onClickMoreBtn')

    def onClickResetBtn(self):
        self._printOverrideError('onClickResetBtn')

    def onClickSettingsBtn(self):
        self._printOverrideError('onClickSettingsBtn')

    def onExpanded(self, value):
        self._printOverrideError('onExpanded')

    def onTabSelected(self, alias):
        self._printOverrideError('onTabSelected')

    def onCounterUpdated(self):
        self._printOverrideError('onCounterUpdated')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setButtonsStateS(self, states):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtonsState(states)

    def as_setHeaderTooltipS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderTooltip(value)