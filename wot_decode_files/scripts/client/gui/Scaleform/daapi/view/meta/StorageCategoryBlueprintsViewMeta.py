# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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