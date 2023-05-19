# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FalloutTankCarouselMeta.py
from gui.Scaleform.daapi.view.lobby.hangar.carousels.basic.tank_carousel import TankCarousel

class FalloutTankCarouselMeta(TankCarousel):

    def changeVehicle(self, id):
        self._printOverrideError('changeVehicle')

    def clearSlot(self, vehicleId):
        self._printOverrideError('clearSlot')

    def shiftSlot(self, vehicleId):
        self._printOverrideError('shiftSlot')

    def as_setMultiselectionInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setMultiselectionInfo(data)

    def as_getMultiselectionDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getMultiselectionDP()