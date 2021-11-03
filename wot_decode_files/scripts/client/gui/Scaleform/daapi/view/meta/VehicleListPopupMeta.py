# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleListPopupMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class VehicleListPopupMeta(AbstractWindowView):

    def onSelectVehicles(self, item):
        self._printOverrideError('onSelectVehicles')

    def applyFilters(self, nation, vehicleType):
        self._printOverrideError('applyFilters')

    def as_setListDataS(self, listData, selectedItems):
        if self._isDAAPIInited():
            return self.flashObject.as_setListData(listData, selectedItems)

    def as_setInfoTextS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setInfoText(text)

    def as_setFiltersDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setFiltersData(data)