# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MessengerBarMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class MessengerBarMeta(BaseDAAPIComponent):

    def channelButtonClick(self):
        self._printOverrideError('channelButtonClick')

    def referralButtonClick(self):
        self._printOverrideError('referralButtonClick')

    def sessionStatsButtonClick(self):
        self._printOverrideError('sessionStatsButtonClick')

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setVehicleCompareCartButtonVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleCompareCartButtonVisible(value)

    def as_setReferralProgramButtonVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setReferralProgramButtonVisible(value)

    def as_setReferralButtonEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setReferralButtonEnabled(value)

    def as_setReferralBtnCounterS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setReferralBtnCounter(value)

    def as_setReferralBtnLimitIndicationS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setReferralBtnLimitIndication(value)

    def as_openVehicleCompareCartPopoverS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_openVehicleCompareCartPopover(value)

    def as_showAddVehicleCompareAnimS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showAddVehicleCompareAnim(data)

    def as_setSessionStatsButtonVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSessionStatsButtonVisible(value)

    def as_setSessionStatsButtonEnableS(self, value, tooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_setSessionStatsButtonEnable(value, tooltip)

    def as_setSessionStatsButtonSettingsUpdateS(self, show, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSessionStatsButtonSettingsUpdate(show, value)