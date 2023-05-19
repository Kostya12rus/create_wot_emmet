# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MissionsVehicleSelectorMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class MissionsVehicleSelectorMeta(BaseDAAPIComponent):

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_showSelectedVehicleS(self, vehData):
        if self._isDAAPIInited():
            return self.flashObject.as_showSelectedVehicle(vehData)

    def as_hideSelectedVehicleS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideSelectedVehicle()

    def as_closeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_close()