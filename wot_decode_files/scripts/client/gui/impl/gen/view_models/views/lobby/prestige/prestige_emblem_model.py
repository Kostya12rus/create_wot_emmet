# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/prestige/prestige_emblem_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class PrestigeLevelGrade(Enum):
    IRON = 'iron'
    BRONZE = 'bronze'
    SILVER = 'silver'
    GOLD = 'gold'
    ENAMEL = 'enamel'
    MAXIMUM = 'prestige'
    UNDEFINED = 'undefined'


class PrestigeEmblemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PrestigeEmblemModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return PrestigeLevelGrade(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)

    def getLevel(self):
        return self._getNumber(1)

    def setLevel(self, value):
        self._setNumber(1, value)

    def getGrade(self):
        return self._getNumber(2)

    def setGrade(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(PrestigeEmblemModel, self)._initialize()
        self._addStringProperty('type')
        self._addNumberProperty('level', 0)
        self._addNumberProperty('grade', -1)