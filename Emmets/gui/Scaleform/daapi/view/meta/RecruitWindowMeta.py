# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RecruitWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class RecruitWindowMeta(AbstractWindowView):

    def updateVehicleClassDropdown(self, nation):
        self._printOverrideError('updateVehicleClassDropdown')

    def updateVehicleTypeDropdown(self, nation, vclass):
        self._printOverrideError('updateVehicleTypeDropdown')

    def updateRoleDropdown(self, nation, vclass, vtype):
        self._printOverrideError('updateRoleDropdown')

    def updateNationDropdown(self):
        self._printOverrideError('updateNationDropdown')

    def buyTankman(self, nationID, typeID, role, studyType, slot):
        self._printOverrideError('buyTankman')

    def updateAllDropdowns(self, nationID, tankType, typeID, roleType):
        self._printOverrideError('updateAllDropdowns')

    def as_setVehicleClassDropdownS(self, vehicleClassData):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleClassDropdown(vehicleClassData)

    def as_setVehicleTypeDropdownS(self, vehicleTypeData):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleTypeDropdown(vehicleTypeData)

    def as_setRoleDropdownS(self, roleData):
        if self._isDAAPIInited():
            return self.flashObject.as_setRoleDropdown(roleData)

    def as_initDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_initData(data)

    def as_setNationsS(self, nationsData):
        if self._isDAAPIInited():
            return self.flashObject.as_setNations(nationsData)

    def as_setRecruitButtonsEnableStateS(self, academyButtonEnabled, schoolButtonEnabled, coursesButtonEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setRecruitButtonsEnableState(academyButtonEnabled, schoolButtonEnabled, coursesButtonEnabled)

    def as_setAllDropdownsS(self, nationsData, vehicleClassData, vehicleTypeData, roleData):
        if self._isDAAPIInited():
            return self.flashObject.as_setAllDropdowns(nationsData, vehicleClassData, vehicleTypeData, roleData)