# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/achievements/tooltips/kpi_tooltip_view_model.py
from frameworks.wulf import ViewModel

class KpiTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(KpiTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getKpiType(self):
        return self._getString(0)

    def setKpiType(self, value):
        self._setString(0, value)

    def getAvgValue(self):
        return self._getString(1)

    def setAvgValue(self, value):
        self._setString(1, value)

    def getMaxValue(self):
        return self._getString(2)

    def setMaxValue(self, value):
        self._setString(2, value)

    def getTankName(self):
        return self._getString(3)

    def setTankName(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(KpiTooltipViewModel, self)._initialize()
        self._addStringProperty('kpiType', 'damage')
        self._addStringProperty('avgValue', '')
        self._addStringProperty('maxValue', '')
        self._addStringProperty('tankName', '')