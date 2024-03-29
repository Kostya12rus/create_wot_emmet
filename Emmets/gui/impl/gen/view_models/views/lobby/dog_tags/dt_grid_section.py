# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/dog_tags/dt_grid_section.py
from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.dog_tags.dt_component import DtComponent

class DtGridSection(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(DtGridSection, self).__init__(properties=properties, commands=commands)

    def getTitle(self):
        return self._getResource(0)

    def setTitle(self, value):
        self._setResource(0, value)

    def getItems(self):
        return self._getArray(1)

    def setItems(self, value):
        self._setArray(1, value)

    @staticmethod
    def getItemsType():
        return DtComponent

    def getTooltipTitle(self):
        return self._getResource(2)

    def setTooltipTitle(self, value):
        self._setResource(2, value)

    def getTooltipDescription(self):
        return self._getResource(3)

    def setTooltipDescription(self, value):
        self._setResource(3, value)

    def _initialize(self):
        super(DtGridSection, self)._initialize()
        self._addResourceProperty('title', R.invalid())
        self._addArrayProperty('items', Array())
        self._addResourceProperty('tooltipTitle', R.invalid())
        self._addResourceProperty('tooltipDescription', R.invalid())