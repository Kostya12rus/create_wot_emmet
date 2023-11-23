# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/common/crew_widget_tankman_skill_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class SkillType(Enum):
    NEW = 'new'
    LEARNED = 'learned'
    LEARNING = 'learning'
    IRRELEVANT = 'irrelevant'
    POSSIBLE = 'possible'


class CrewWidgetTankmanSkillModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(CrewWidgetTankmanSkillModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getIcon(self):
        return self._getString(1)

    def setIcon(self, value):
        self._setString(1, value)

    def getType(self):
        return SkillType(self._getString(2))

    def setType(self, value):
        self._setString(2, value.value)

    def _initialize(self):
        super(CrewWidgetTankmanSkillModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addStringProperty('icon', '')
        self._addStringProperty('type')