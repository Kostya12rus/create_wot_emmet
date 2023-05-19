# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StorageCategoryBlueprintsViewMeta.py
from gui.Scaleform.daapi.view.lobby.storage.vehicle_view import VehicleView

class StorageCategoryBlueprintsViewMeta(VehicleView):

    def navigateToBlueprintScreen(self, itemId):
        self._printOverrideError('navigateToBlueprintScreen')

    def selectConvertible(self, value):
        self._printOverrideError('selectConvertible')

    def as_updateIntelligenceDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateIntelligenceData(data)

    def as_updateNationalFragmentsS(self, fragments):
        if self._isDAAPIInited():
            return self.flashObject.as_updateNationalFragments(fragments)

    def as_updateCanConvertS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCanConvert(value)