# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/tooltip/modifier_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class ModifierModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ModifierModel, self).__init__(properties=properties, commands=commands)

    def getValue(self):
        return self._getNumber(0)

    def setValue(self, value):
        self._setNumber(0, value)

    def getNameRes(self):
        return self._getResource(1)

    def setNameRes(self, value):
        self._setResource(1, value)

    def getUnitRes(self):
        return self._getResource(2)

    def setUnitRes(self, value):
        self._setResource(2, value)

    def _initialize(self):
        super(ModifierModel, self)._initialize()
        self._addNumberProperty('value', 0)
        self._addResourceProperty('nameRes', R.invalid())
        self._addResourceProperty('unitRes', R.invalid())