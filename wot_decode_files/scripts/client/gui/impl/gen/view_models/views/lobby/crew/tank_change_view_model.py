# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/tank_change_view_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.crew.common.base_crew_view_model import BaseCrewViewModel
from gui.impl.gen.view_models.views.lobby.crew.tank_change_vehicle_model import TankChangeVehicleModel

class TankChangeViewModel(BaseCrewViewModel):
    __slots__ = ('onVehicleSelected', 'onResetFilters')

    def __init__(self, properties=4, commands=6):
        super(TankChangeViewModel, self).__init__(properties=properties, commands=commands)

    def getNation(self):
        return self._getString(2)

    def setNation(self, value):
        self._setString(2, value)

    def getVehicleList(self):
        return self._getArray(3)

    def setVehicleList(self, value):
        self._setArray(3, value)

    @staticmethod
    def getVehicleListType():
        return TankChangeVehicleModel

    def _initialize(self):
        super(TankChangeViewModel, self)._initialize()
        self._addStringProperty('nation', '')
        self._addArrayProperty('vehicleList', Array())
        self.onVehicleSelected = self._addCommand('onVehicleSelected')
        self.onResetFilters = self._addCommand('onResetFilters')