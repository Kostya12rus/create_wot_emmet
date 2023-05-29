# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/nation_change/nation_change_supply_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class NationChangeSupplyModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(NationChangeSupplyModel, self).__init__(properties=properties, commands=commands)

    def getImage(self):
        return self._getResource(0)

    def setImage(self, value):
        self._setResource(0, value)

    def getIntCD(self):
        return self._getNumber(1)

    def setIntCD(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(NationChangeSupplyModel, self)._initialize()
        self._addResourceProperty('image', R.invalid())
        self._addNumberProperty('intCD', 0)