# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StorageCategoryForSellViewMeta.py
from gui.Scaleform.daapi.view.lobby.storage.category_view import InventoryCategoryView

class StorageCategoryForSellViewMeta(InventoryCategoryView):

    def navigateToStore(self):
        self._printOverrideError('navigateToStore')

    def selectItem(self, itemId, isSelected):
        self._printOverrideError('selectItem')

    def selectAll(self, isSelected):
        self._printOverrideError('selectAll')

    def sellItem(self, itemId):
        self._printOverrideError('sellItem')

    def sellAll(self):
        self._printOverrideError('sellAll')

    def as_initS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_init(data)