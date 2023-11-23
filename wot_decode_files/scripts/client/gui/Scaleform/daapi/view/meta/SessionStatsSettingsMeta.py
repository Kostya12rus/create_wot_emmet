# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SessionStatsSettingsMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class SessionStatsSettingsMeta(BaseDAAPIComponent):

    def onClickApplyBtn(self):
        self._printOverrideError('onClickApplyBtn')

    def onClickBackBtn(self):
        self._printOverrideError('onClickBackBtn')

    def onClickResetBtn(self):
        self._printOverrideError('onClickResetBtn')

    def onSettingsInputChanged(self, identifier, value):
        self._printOverrideError('onSettingsInputChanged')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setControlsStateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setControlsState(data)

    def as_setBattleSettingsStatusS(self, value, showWarning):
        if self._isDAAPIInited():
            return self.flashObject.as_setBattleSettingsStatus(value, showWarning)