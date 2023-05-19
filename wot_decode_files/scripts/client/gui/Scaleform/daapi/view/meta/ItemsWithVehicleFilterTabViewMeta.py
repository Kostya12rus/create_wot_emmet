# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ItemsWithVehicleFilterTabViewMeta.py
from gui.Scaleform.daapi.view.lobby.storage.inventory.filters.filter_by_type import FiltrableInventoryCategoryByTypeTabView

class ItemsWithVehicleFilterTabViewMeta(FiltrableInventoryCategoryByTypeTabView):

    def resetVehicleFilter(self):
        self._printOverrideError('resetVehicleFilter')

    def as_initVehicleFilterS(self, vehicleFilterVO):
        if self._isDAAPIInited():
            return self.flashObject.as_initVehicleFilter(vehicleFilterVO)

    def as_updateVehicleFilterButtonS(self, vehicleFilterVO):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicleFilterButton(vehicleFilterVO)