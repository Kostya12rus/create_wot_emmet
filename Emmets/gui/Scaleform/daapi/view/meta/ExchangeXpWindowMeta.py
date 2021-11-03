# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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