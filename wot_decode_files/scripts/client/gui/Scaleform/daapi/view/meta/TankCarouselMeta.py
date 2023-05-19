# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TankCarouselMeta.py
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_environment import CarouselEnvironment

class TankCarouselMeta(CarouselEnvironment):

    def restoreTank(self):
        self._printOverrideError('restoreTank')

    def buyTank(self):
        self._printOverrideError('buyTank')

    def buySlot(self):
        self._printOverrideError('buySlot')

    def buyRentPromotion(self, intCD):
        self._printOverrideError('buyRentPromotion')

    def selectWotPlusVehicle(self, intCD):
        self._printOverrideError('selectWotPlusVehicle')

    def getCarouselAlias(self):
        self._printOverrideError('getCarouselAlias')

    def setFilter(self, id):
        self._printOverrideError('setFilter')

    def as_rowCountS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_rowCount(value)

    def as_setSmallDoubleCarouselS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSmallDoubleCarousel(value)

    def as_useExtendedCarouselS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_useExtendedCarousel(value)

    def as_scrollToSlotS(self, slotIdx):
        if self._isDAAPIInited():
            return self.flashObject.as_scrollToSlot(slotIdx)