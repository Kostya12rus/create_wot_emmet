# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PersonalMissionsAwardsViewMeta.py
from gui.Scaleform.framework.entities.View import View

class PersonalMissionsAwardsViewMeta(View):

    def showVehiclePreview(self):
        self._printOverrideError('showVehiclePreview')

    def closeView(self):
        self._printOverrideError('closeView')

    def showMissionByVehicleType(self, vehicleType):
        self._printOverrideError('showMissionByVehicleType')

    def buyMissionsByVehicleType(self, vehicleType):
        self._printOverrideError('buyMissionsByVehicleType')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setHeaderDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderData(data)