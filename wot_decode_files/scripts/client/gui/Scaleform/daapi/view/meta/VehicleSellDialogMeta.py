# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleSellDialogMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class VehicleSellDialogMeta(AbstractWindowView):

    def setDialogSettings(self, isOpen):
        self._printOverrideError('setDialogSettings')

    def sell(self):
        self._printOverrideError('sell')

    def setUserInput(self, value):
        self._printOverrideError('setUserInput')

    def setCrewDismissal(self, value):
        self._printOverrideError('setCrewDismissal')

    def onSelectionChanged(self, itemID, toInventory, currency):
        self._printOverrideError('onSelectionChanged')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_visibleControlBlockS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_visibleControlBlock(value)

    def as_enableButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enableButton(value)

    def as_setControlQuestionDataS(self, isGold, value, question):
        if self._isDAAPIInited():
            return self.flashObject.as_setControlQuestionData(isGold, value, question)

    def as_setTotalS(self, common, total):
        if self._isDAAPIInited():
            return self.flashObject.as_setTotal(common, total)

    def as_updateAccountMoneyS(self, currency, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateAccountMoney(currency, value)