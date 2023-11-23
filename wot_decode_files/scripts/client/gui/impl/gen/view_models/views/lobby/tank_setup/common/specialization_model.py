# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/common/specialization_model.py
from frameworks.wulf import ViewModel

class SpecializationModel(ViewModel):
    __slots__ = ()
    EMPTY = 'empty'

    def __init__(self, properties=3, commands=0):
        super(SpecializationModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getIsCorrect(self):
        return self._getBool(1)

    def setIsCorrect(self, value):
        self._setBool(1, value)

    def getIsClickable(self):
        return self._getBool(2)

    def setIsClickable(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(SpecializationModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addBoolProperty('isCorrect', False)
        self._addBoolProperty('isClickable', False)