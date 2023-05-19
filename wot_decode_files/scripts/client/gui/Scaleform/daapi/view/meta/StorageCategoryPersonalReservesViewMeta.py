# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StorageCategoryPersonalReservesViewMeta.py
from gui.Scaleform.daapi.view.lobby.storage.category_view import BaseCategoryView

class StorageCategoryPersonalReservesViewMeta(BaseCategoryView):

    def navigateToStore(self):
        self._printOverrideError('navigateToStore')

    def activateReserve(self, boosterId):
        self._printOverrideError('activateReserve')

    def resetFilter(self):
        self._printOverrideError('resetFilter')

    def onFiltersChange(self, filters):
        self._printOverrideError('onFiltersChange')

    def onInfoClicked(self):
        self._printOverrideError('onInfoClicked')

    def as_initS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_init(data)

    def as_initFilterS(self, typeFiltersVO):
        if self._isDAAPIInited():
            return self.flashObject.as_initFilter(typeFiltersVO)

    def as_resetFilterS(self, resetData):
        if self._isDAAPIInited():
            return self.flashObject.as_resetFilter(resetData)

    def as_updateCounterS(self, shouldShow, displayString, isZeroCount):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCounter(shouldShow, displayString, isZeroCount)