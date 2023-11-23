# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/collection/page_backgrounds_model.py
from frameworks.wulf import ViewModel

class PageBackgroundsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(PageBackgroundsModel, self).__init__(properties=properties, commands=commands)

    def getMain(self):
        return self._getString(0)

    def setMain(self, value):
        self._setString(0, value)

    def getLogicalCircuit(self):
        return self._getString(1)

    def setLogicalCircuit(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(PageBackgroundsModel, self)._initialize()
        self._addStringProperty('main', '')
        self._addStringProperty('logicalCircuit', '')