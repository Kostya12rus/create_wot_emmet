# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleSelectPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class VehicleSelectPopoverMeta(SmartPopOverView):

    def setVehicleSelected(self, dbID, autoClose):
        self._printOverrideError('setVehicleSelected')

    def applyFilters(self, nation, vehicleType, level, isMain, hangarOnly):
        self._printOverrideError('applyFilters')

    def addButtonClicked(self):
        self._printOverrideError('addButtonClicked')

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_getTableDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getTableDP()

    def as_setAddButtonStateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setAddButtonState(data)

    def as_updateTableSortFieldS(self, sortField, sortDirection):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTableSortField(sortField, sortDirection)