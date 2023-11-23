# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/dog_tags/dt_component_layout.py
from frameworks.wulf import ViewModel

class DtComponentLayout(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(DtComponentLayout, self).__init__(properties=properties, commands=commands)

    def getMarginX(self):
        return self._getReal(0)

    def setMarginX(self, value):
        self._setReal(0, value)

    def getMarginY(self):
        return self._getReal(1)

    def setMarginY(self, value):
        self._setReal(1, value)

    def _initialize(self):
        super(DtComponentLayout, self)._initialize()
        self._addRealProperty('marginX', 0.0)
        self._addRealProperty('marginY', 0.0)