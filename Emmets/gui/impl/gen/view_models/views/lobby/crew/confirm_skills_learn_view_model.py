# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/confirm_skills_learn_view_model.py
from frameworks.wulf import ViewModel

class ConfirmSkillsLearnViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(ConfirmSkillsLearnViewModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getAmount(self):
        return self._getNumber(1)

    def setAmount(self, value):
        self._setNumber(1, value)

    def getSkill(self):
        return self._getString(2)

    def setSkill(self, value):
        self._setString(2, value)

    def getIcon(self):
        return self._getString(3)

    def setIcon(self, value):
        self._setString(3, value)

    def getProgress(self):
        return self._getNumber(4)

    def setProgress(self, value):
        self._setNumber(4, value)

    def getRole(self):
        return self._getString(5)

    def setRole(self, value):
        self._setString(5, value)

    def _initialize(self):
        super(ConfirmSkillsLearnViewModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addNumberProperty('amount', 0)
        self._addStringProperty('skill', '')
        self._addStringProperty('icon', '')
        self._addNumberProperty('progress', 0)
        self._addStringProperty('role', '')