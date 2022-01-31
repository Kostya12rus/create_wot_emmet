# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/new_year/tooltips/ny_mega_toy_tooltip_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class NyMegaToyTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(NyMegaToyTooltipModel, self).__init__(properties=properties, commands=commands)

    def getTypeIcon(self):
        return self._getResource(0)

    def setTypeIcon(self, value):
        self._setResource(0, value)

    def getName(self):
        return self._getResource(1)

    def setName(self, value):
        self._setResource(1, value)

    def getDescription(self):
        return self._getResource(2)

    def setDescription(self, value):
        self._setResource(2, value)

    def getShardsPrice(self):
        return self._getNumber(3)

    def setShardsPrice(self, value):
        self._setNumber(3, value)

    def getBonus(self):
        return self._getReal(4)

    def setBonus(self, value):
        self._setReal(4, value)

    def getIcon(self):
        return self._getResource(5)

    def setIcon(self, value):
        self._setResource(5, value)

    def _initialize(self):
        super(NyMegaToyTooltipModel, self)._initialize()
        self._addResourceProperty('typeIcon', R.invalid())
        self._addResourceProperty('name', R.invalid())
        self._addResourceProperty('description', R.invalid())
        self._addNumberProperty('shardsPrice', 0)
        self._addRealProperty('bonus', 0.0)
        self._addResourceProperty('icon', R.invalid())