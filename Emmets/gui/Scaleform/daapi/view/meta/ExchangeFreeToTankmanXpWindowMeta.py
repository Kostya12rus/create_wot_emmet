# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ExchangeFreeToTankmanXpWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ExchangeFreeToTankmanXpWindowMeta(AbstractWindowView):

    def apply(self):
        self._printOverrideError('apply')

    def onValueChanged(self, data):
        self._printOverrideError('onValueChanged')

    def calcValueRequest(self, value):
        self._printOverrideError('calcValueRequest')

    def as_setInitDataS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(value)

    def as_setCalcValueResponseS(self, price, actionPriceData):
        if self._isDAAPIInited():
            return self.flashObject.as_setCalcValueResponse(price, actionPriceData)

    def as_setWalletStatusS(self, walletStatus):
        if self._isDAAPIInited():
            return self.flashObject.as_setWalletStatus(walletStatus)