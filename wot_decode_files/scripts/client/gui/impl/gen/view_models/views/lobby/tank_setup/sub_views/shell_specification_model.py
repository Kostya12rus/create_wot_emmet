# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/shell_specification_model.py
from frameworks.wulf import ViewModel

class ShellSpecificationModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ShellSpecificationModel, self).__init__(properties=properties, commands=commands)

    def getParamName(self):
        return self._getString(0)

    def setParamName(self, value):
        self._setString(0, value)

    def getValue(self):
        return self._getString(1)

    def setValue(self, value):
        self._setString(1, value)

    def getMetricValue(self):
        return self._getString(2)

    def setMetricValue(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(ShellSpecificationModel, self)._initialize()
        self._addStringProperty('paramName', '')
        self._addStringProperty('value', '')
        self._addStringProperty('metricValue', '')