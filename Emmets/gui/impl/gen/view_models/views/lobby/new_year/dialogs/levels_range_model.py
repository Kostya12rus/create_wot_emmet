# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/new_year/dialogs/levels_range_model.py
from frameworks.wulf import ViewModel

class LevelsRangeModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(LevelsRangeModel, self).__init__(properties=properties, commands=commands)

    def getStartLevel(self):
        return self._getNumber(0)

    def setStartLevel(self, value):
        self._setNumber(0, value)

    def getCurrentLevel(self):
        return self._getNumber(1)

    def setCurrentLevel(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(LevelsRangeModel, self)._initialize()
        self._addNumberProperty('startLevel', 0)
        self._addNumberProperty('currentLevel', 0)