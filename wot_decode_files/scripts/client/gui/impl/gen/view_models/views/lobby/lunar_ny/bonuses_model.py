# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/lunar_ny/bonuses_model.py
from frameworks.wulf import ViewModel

class BonusesModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(BonusesModel, self).__init__(properties=properties, commands=commands)

    def getCombatExperience(self):
        return self._getNumber(0)

    def setCombatExperience(self, value):
        self._setNumber(0, value)

    def getCredits(self):
        return self._getNumber(1)

    def setCredits(self, value):
        self._setNumber(1, value)

    def getCrewExperience(self):
        return self._getNumber(2)

    def setCrewExperience(self, value):
        self._setNumber(2, value)

    def getFreeExperience(self):
        return self._getNumber(3)

    def setFreeExperience(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(BonusesModel, self)._initialize()
        self._addNumberProperty('combatExperience', -1)
        self._addNumberProperty('credits', -1)
        self._addNumberProperty('crewExperience', -1)
        self._addNumberProperty('freeExperience', -1)