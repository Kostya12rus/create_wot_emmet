# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ItemsWithTypeFilterTabViewMeta.py
from gui.Scaleform.daapi.view.lobby.storage.inventory.inventory_view import InventoryCategoryView

class ItemsWithTypeFilterTabViewMeta(InventoryCategoryView):

    def sellItem(self, itemId):
        self._printOverrideError('sellItem')

    def resetFilter(self):
        self._printOverrideError('resetFilter')

    def onFiltersChange(self, filters):
        self._printOverrideError('onFiltersChange')

    def navigateToStore(self):
        self._printOverrideError('navigateToStore')

    def upgradeItem(self, itemId):
        self._printOverrideError('upgradeItem')

    def as_initTypeFilterS(self, typeFiltersVO):
        if self._isDAAPIInited():
            return self.flashObject.as_initTypeFilter(typeFiltersVO)

    def as_resetFilterS(self, resetData):
        if self._isDAAPIInited():
            return self.flashObject.as_resetFilter(resetData)

    def as_updateCounterS(self, shouldShow, displayString, isZeroCount):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCounter(shouldShow, displayString, isZeroCount)