# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/common/crew_widget_tankman_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.crew_widget_tankman_skill_model import CrewWidgetTankmanSkillModel

class CrewWidgetTankmanModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=21, commands=0):
        super(CrewWidgetTankmanModel, self).__init__(properties=properties, commands=commands)

    def getTankmanID(self):
        return self._getNumber(0)

    def setTankmanID(self, value):
        self._setNumber(0, value)

    def getFullName(self):
        return self._getString(1)

    def setFullName(self, value):
        self._setString(1, value)

    def getIcon(self):
        return self._getString(2)

    def setIcon(self, value):
        self._setString(2, value)

    def getSpecializationLevel(self):
        return self._getNumber(3)

    def setSpecializationLevel(self, value):
        self._setNumber(3, value)

    def getBaseSpecializationLevel(self):
        return self._getNumber(4)

    def setBaseSpecializationLevel(self, value):
        self._setNumber(4, value)

    def getRoles(self):
        return self._getArray(5)

    def setRoles(self, value):
        self._setArray(5, value)

    @staticmethod
    def getRolesType():
        return unicode

    def getSkills(self):
        return self._getArray(6)

    def setSkills(self, value):
        self._setArray(6, value)

    @staticmethod
    def getSkillsType():
        return CrewWidgetTankmanSkillModel

    def getNewSkillsAmount(self):
        return self._getNumber(7)

    def setNewSkillsAmount(self, value):
        self._setNumber(7, value)

    def getPossibleSkillsAmount(self):
        return self._getNumber(8)

    def setPossibleSkillsAmount(self, value):
        self._setNumber(8, value)

    def getLastPossibleSkillLevel(self):
        return self._getReal(9)

    def setLastPossibleSkillLevel(self, value):
        self._setReal(9, value)

    def getHasPossibleProgress(self):
        return self._getBool(10)

    def setHasPossibleProgress(self, value):
        self._setBool(10, value)

    def getLastSkillLevel(self):
        return self._getReal(11)

    def setLastSkillLevel(self, value):
        self._setReal(11, value)

    def getLastRoleLevel(self):
        return self._getReal(12)

    def setLastRoleLevel(self, value):
        self._setReal(12, value)

    def getLastPossibleRoleLevel(self):
        return self._getReal(13)

    def setLastPossibleRoleLevel(self, value):
        self._setReal(13, value)

    def getLastSkillLevelFull(self):
        return self._getReal(14)

    def setLastSkillLevelFull(self, value):
        self._setReal(14, value)

    def getIsLessMastered(self):
        return self._getBool(15)

    def setIsLessMastered(self, value):
        self._setBool(15, value)

    def getIsInSkin(self):
        return self._getBool(16)

    def setIsInSkin(self, value):
        self._setBool(16, value)

    def getIsFemale(self):
        return self._getBool(17)

    def setIsFemale(self, value):
        self._setBool(17, value)

    def getIsUntrained(self):
        return self._getBool(18)

    def setIsUntrained(self, value):
        self._setBool(18, value)

    def getHasWarning(self):
        return self._getBool(19)

    def setHasWarning(self, value):
        self._setBool(19, value)

    def getIsInteractive(self):
        return self._getBool(20)

    def setIsInteractive(self, value):
        self._setBool(20, value)

    def _initialize(self):
        super(CrewWidgetTankmanModel, self)._initialize()
        self._addNumberProperty('tankmanID', 0)
        self._addStringProperty('fullName', '')
        self._addStringProperty('icon', '')
        self._addNumberProperty('specializationLevel', 0)
        self._addNumberProperty('baseSpecializationLevel', 0)
        self._addArrayProperty('roles', Array())
        self._addArrayProperty('skills', Array())
        self._addNumberProperty('newSkillsAmount', 0)
        self._addNumberProperty('possibleSkillsAmount', 0)
        self._addRealProperty('lastPossibleSkillLevel', -1)
        self._addBoolProperty('hasPossibleProgress', False)
        self._addRealProperty('lastSkillLevel', 0.0)
        self._addRealProperty('lastRoleLevel', 0.0)
        self._addRealProperty('lastPossibleRoleLevel', 0.0)
        self._addRealProperty('lastSkillLevelFull', 0.0)
        self._addBoolProperty('isLessMastered', False)
        self._addBoolProperty('isInSkin', False)
        self._addBoolProperty('isFemale', False)
        self._addBoolProperty('isUntrained', False)
        self._addBoolProperty('hasWarning', False)
        self._addBoolProperty('isInteractive', False)