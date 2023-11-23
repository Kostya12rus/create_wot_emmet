# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/common/role_skill_slot_model.py
from frameworks.wulf import ViewModel

class RoleSkillSlotModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(RoleSkillSlotModel, self).__init__(properties=properties, commands=commands)

    def getRoleSkill(self):
        return self._getString(0)

    def setRoleSkill(self, value):
        self._setString(0, value)

    def getTooltipId(self):
        return self._getString(1)

    def setTooltipId(self, value):
        self._setString(1, value)

    def getTooltipHeader(self):
        return self._getString(2)

    def setTooltipHeader(self, value):
        self._setString(2, value)

    def getTooltipBody(self):
        return self._getString(3)

    def setTooltipBody(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(RoleSkillSlotModel, self)._initialize()
        self._addStringProperty('roleSkill', '')
        self._addStringProperty('tooltipId', '')
        self._addStringProperty('tooltipHeader', '')
        self._addStringProperty('tooltipBody', '')