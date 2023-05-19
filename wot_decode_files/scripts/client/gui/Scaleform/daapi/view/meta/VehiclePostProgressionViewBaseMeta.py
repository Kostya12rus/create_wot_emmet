# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehiclePostProgressionViewBaseMeta.py
from gui.Scaleform.framework.entities.View import View

class VehiclePostProgressionViewBaseMeta(View):

    def demountAllPairs(self):
        self._printOverrideError('demountAllPairs')

    def as_setVehicleTitleS(self, vo):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleTitle(vo)

    def as_setDataS(self, vo):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(vo)

    def as_showS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_show()

    def as_onEscPressedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_onEscPressed()