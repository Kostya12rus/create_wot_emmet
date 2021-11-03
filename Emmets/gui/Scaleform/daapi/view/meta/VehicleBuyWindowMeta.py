# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleBuyWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class VehicleBuyWindowMeta(AbstractWindowView):

    def submit(self, data):
        self._printOverrideError('submit')

    def stateChange(self, data):
        self._printOverrideError('stateChange')

    def selectTab(self, tabIndex):
        self._printOverrideError('selectTab')

    def onTradeInClearVehicle(self):
        self._printOverrideError('onTradeInClearVehicle')

    def as_setGoldS(self, gold):
        if self._isDAAPIInited():
            return self.flashObject.as_setGold(gold)

    def as_setCreditsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCredits(value)

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_updateTradeOffVehicleS(self, vehicleBuyTradeOffVo):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTradeOffVehicle(vehicleBuyTradeOffVo)

    def as_setTradeInWarningMessagegeS(self, message):
        if self._isDAAPIInited():
            return self.flashObject.as_setTradeInWarningMessagege(message)

    def as_setStateS(self, academyEnabled, schoolEnabled, freeEnabled, submitEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setState(academyEnabled, schoolEnabled, freeEnabled, submitEnabled)