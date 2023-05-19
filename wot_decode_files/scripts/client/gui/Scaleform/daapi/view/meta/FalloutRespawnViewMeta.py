# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FalloutRespawnViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FalloutRespawnViewMeta(BaseDAAPIComponent):

    def onVehicleSelected(self, vehicleID):
        self._printOverrideError('onVehicleSelected')

    def onPostmortemBtnClick(self):
        self._printOverrideError('onPostmortemBtnClick')

    def as_initializeComponentS(self, mainData, slotsData):
        if self._isDAAPIInited():
            return self.flashObject.as_initializeComponent(mainData, slotsData)

    def as_updateTimerS(self, mainTimer, slotsStateData):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTimer(mainTimer, slotsStateData)

    def as_updateS(self, selectedVehicleName, slotsStateData):
        if self._isDAAPIInited():
            return self.flashObject.as_update(selectedVehicleName, slotsStateData)

    def as_showGasAttackModeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showGasAttackMode()