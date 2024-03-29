# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RosterSlotSettingsWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class RosterSlotSettingsWindowMeta(AbstractWindowView):

    def onFiltersUpdate(self, nation, vehicleType, isMain, level, compatibleOnly):
        self._printOverrideError('onFiltersUpdate')

    def requestVehicleFilters(self):
        self._printOverrideError('requestVehicleFilters')

    def submitButtonHandler(self, value):
        self._printOverrideError('submitButtonHandler')

    def cancelButtonHandler(self):
        self._printOverrideError('cancelButtonHandler')

    def as_setVehicleSelectionS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleSelection(data)

    def as_setRangeSelectionS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setRangeSelection(data)

    def as_resetSelectionS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_resetSelection()

    def as_selectTabS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_selectTab(index)

    def as_setListDataS(self, listData):
        if self._isDAAPIInited():
            return self.flashObject.as_setListData(listData)

    def as_setStaticDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(data)

    def as_setRosterLimitsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setRosterLimits(data)

    def as_updateVehicleFiltersS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicleFilters(data)