# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ResearchViewMeta.py
from gui.Scaleform.framework.entities.View import View

class ResearchViewMeta(View):

    def request4Buy(self, itemCD):
        self._printOverrideError('request4Buy')

    def request4Info(self, itemCD, rootCD):
        self._printOverrideError('request4Info')

    def request4Restore(self, itemCD):
        self._printOverrideError('request4Restore')

    def showSystemMessage(self, typeString, message):
        self._printOverrideError('showSystemMessage')

    def goToBlueprintView(self, itemCD):
        self._printOverrideError('goToBlueprintView')

    def goToNationChangeView(self, itemCD):
        self._printOverrideError('goToNationChangeView')

    def goToVehicleCollection(self, nation):
        self._printOverrideError('goToVehicleCollection')

    def as_setNodesStatesS(self, primary, data, isRequiredInvalidation=False):
        if self._isDAAPIInited():
            return self.flashObject.as_setNodesStates(primary, data, isRequiredInvalidation)

    def as_setNext2UnlockS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setNext2Unlock(data)

    def as_setVehicleTypeXPS(self, xps):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleTypeXP(xps)

    def as_setInventoryItemsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInventoryItems(data)

    def as_setNodeVehCompareDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setNodeVehCompareData(data)