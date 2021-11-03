# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CustomizationFiltersPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class CustomizationFiltersPopoverMeta(SmartPopOverView):

    def changeGroup(self, itemId):
        self._printOverrideError('changeGroup')

    def setDefaultFilter(self):
        self._printOverrideError('setDefaultFilter')

    def setShowOnlyHistoric(self, value):
        self._printOverrideError('setShowOnlyHistoric')

    def setShowOnlyAcquired(self, value):
        self._printOverrideError('setShowOnlyAcquired')

    def setHideOnAnotherVeh(self, value):
        self._printOverrideError('setHideOnAnotherVeh')

    def setShowOnlyProgressionDecals(self, value):
        self._printOverrideError('setShowOnlyProgressionDecals')

    def setShowOnlyEditableStyles(self, value):
        self._printOverrideError('setShowOnlyEditableStyles')

    def onFilterChange(self, index, value):
        self._printOverrideError('onFilterChange')

    def onFormChange(self, index, value):
        self._printOverrideError('onFormChange')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_enableDefBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enableDefBtn(value)