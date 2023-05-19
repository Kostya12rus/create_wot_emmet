# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/resource_well/tooltips/max_progress_tooltip_model.py
from frameworks.wulf import ViewModel

class MaxProgressTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(MaxProgressTooltipModel, self).__init__(properties=properties, commands=commands)

    def getCurrentValue(self):
        return self._getReal(0)

    def setCurrentValue(self, value):
        self._setReal(0, value)

    def getMaxValue(self):
        return self._getReal(1)

    def setMaxValue(self, value):
        self._setReal(1, value)

    def getResourceType(self):
        return self._getString(2)

    def setResourceType(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(MaxProgressTooltipModel, self)._initialize()
        self._addRealProperty('currentValue', 0.0)
        self._addRealProperty('maxValue', 0.0)
        self._addStringProperty('resourceType', '')