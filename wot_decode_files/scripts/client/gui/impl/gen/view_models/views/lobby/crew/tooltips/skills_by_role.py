# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/tooltips/skills_by_role.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class SkillsByRole(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(SkillsByRole, self).__init__(properties=properties, commands=commands)

    def getRole(self):
        return self._getString(0)

    def setRole(self, value):
        self._setString(0, value)

    def getSkills(self):
        return self._getArray(1)

    def setSkills(self, value):
        self._setArray(1, value)

    @staticmethod
    def getSkillsType():
        return unicode

    def _initialize(self):
        super(SkillsByRole, self)._initialize()
        self._addStringProperty('role', '')
        self._addArrayProperty('skills', Array())