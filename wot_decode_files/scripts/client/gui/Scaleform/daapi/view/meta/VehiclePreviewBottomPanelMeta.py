# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehiclePreviewBottomPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class VehiclePreviewBottomPanelMeta(BaseDAAPIComponent):

    def onBuyOrResearchClick(self):
        self._printOverrideError('onBuyOrResearchClick')

    def onCarouselVehicleSelected(self, intCD):
        self._printOverrideError('onCarouselVehicleSelected')

    def onOfferSelected(self, offerID):
        self._printOverrideError('onOfferSelected')

    def showTooltip(self, intCD, itemType):
        self._printOverrideError('showTooltip')

    def updateData(self, useCompactData):
        self._printOverrideError('updateData')

    def onCouponSelected(self, isActive):
        self._printOverrideError('onCouponSelected')

    def as_setBuyDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBuyData(data)

    def as_setSetItemsDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setSetItemsData(data)

    def as_setCouponS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoupon(data)

    def as_setSetVehiclesDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setSetVehiclesData(data)

    def as_setOffersDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setOffersData(data)

    def as_setSetTitleTooltipS(self, tooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_setSetTitleTooltip(tooltip)

    def as_updateLeftTimeS(self, formattedTime, hasHoursAndMinutes=False):
        if self._isDAAPIInited():
            return self.flashObject.as_updateLeftTime(formattedTime, hasHoursAndMinutes)