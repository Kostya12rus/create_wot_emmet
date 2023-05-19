# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ExchangeXpWindowMeta.py
from gui.Scaleform.daapi.view.lobby.exchange.BaseExchangeWindow import BaseExchangeWindow

class ExchangeXpWindowMeta(BaseExchangeWindow):

    def getSubmitButtonEnableState(self, selectedXPCount):
        self._printOverrideError('getSubmitButtonEnableState')

    def as_vehiclesDataChangedS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_vehiclesDataChanged(data)

    def as_totalExperienceChangedS(self, totalXP):
        if self._isDAAPIInited():
            return self.flashObject.as_totalExperienceChanged(totalXP)

    def as_setWalletStatusS(self, walletStatus, enableSubmitButton):
        if self._isDAAPIInited():
            return self.flashObject.as_setWalletStatus(walletStatus, enableSubmitButton)

    def as_setTargetXPS(self, targetXP):
        if self._isDAAPIInited():
            return self.flashObject.as_setTargetXP(targetXP)