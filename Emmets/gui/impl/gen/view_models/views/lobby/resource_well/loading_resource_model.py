# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/resource_well/loading_resource_model.py
from frameworks.wulf import ViewModel

class LoadingResourceModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(LoadingResourceModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)

    def getSubType(self):
        return self._getString(1)

    def setSubType(self, value):
        self._setString(1, value)

    def getCount(self):
        return self._getNumber(2)

    def setCount(self, value):
        self._setNumber(2, value)

    def getTooltipId(self):
        return self._getString(3)

    def setTooltipId(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(LoadingResourceModel, self)._initialize()
        self._addStringProperty('type', '')
        self._addStringProperty('subType', '')
        self._addNumberProperty('count', 0)
        self._addStringProperty('tooltipId', '')