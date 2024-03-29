# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tooltips/veh_post_progression_entry_point_tooltip_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class VehPostProgressionEntryPointTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(VehPostProgressionEntryPointTooltipModel, self).__init__(properties=properties, commands=commands)

    def getModulesExplored(self):
        return self._getNumber(0)

    def setModulesExplored(self, value):
        self._setNumber(0, value)

    def getModulesTotal(self):
        return self._getNumber(1)

    def setModulesTotal(self, value):
        self._setNumber(1, value)

    def getHeader(self):
        return self._getResource(2)

    def setHeader(self, value):
        self._setResource(2, value)

    def getDescription(self):
        return self._getResource(3)

    def setDescription(self, value):
        self._setResource(3, value)

    def getStatus(self):
        return self._getResource(4)

    def setStatus(self, value):
        self._setResource(4, value)

    def getHasVehiclesToUnlock(self):
        return self._getBool(5)

    def setHasVehiclesToUnlock(self, value):
        self._setBool(5, value)

    def _initialize(self):
        super(VehPostProgressionEntryPointTooltipModel, self)._initialize()
        self._addNumberProperty('modulesExplored', 0)
        self._addNumberProperty('modulesTotal', 0)
        self._addResourceProperty('header', R.invalid())
        self._addResourceProperty('description', R.invalid())
        self._addResourceProperty('status', R.invalid())
        self._addBoolProperty('hasVehiclesToUnlock', False)