# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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

    def as_initS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_init(data)

    def as_initFilterS(self, typeFiltersVO, durationFiltersVO):
        if self._isDAAPIInited():
            return self.flashObject.as_initFilter(typeFiltersVO, durationFiltersVO)

    def as_resetFilterS(self, resetData):
        if self._isDAAPIInited():
            return self.flashObject.as_resetFilter(resetData)

    def as_updateCounterS(self, shouldShow, displayString, isZeroCount):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCounter(shouldShow, displayString, isZeroCount)