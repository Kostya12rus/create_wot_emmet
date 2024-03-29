# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_matters/battle_matters_vehicle_selection_view_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_matters.battle_matters_vehicle_model import BattleMattersVehicleModel

class BattleMattersVehicleSelectionViewModel(ViewModel):
    __slots__ = ('onGoBack', 'onShowVehicle', 'onCompareVehicle', 'onResetFilter')
    ARG_VEHICLE_ID = 'vehCD'

    def __init__(self, properties=3, commands=4):
        super(BattleMattersVehicleSelectionViewModel, self).__init__(properties=properties, commands=commands)

    def getEndDate(self):
        return self._getNumber(0)

    def setEndDate(self, value):
        self._setNumber(0, value)

    def getTotalVehiclesCount(self):
        return self._getNumber(1)

    def setTotalVehiclesCount(self, value):
        self._setNumber(1, value)

    def getVehicles(self):
        return self._getArray(2)

    def setVehicles(self, value):
        self._setArray(2, value)

    @staticmethod
    def getVehiclesType():
        return BattleMattersVehicleModel

    def _initialize(self):
        super(BattleMattersVehicleSelectionViewModel, self)._initialize()
        self._addNumberProperty('endDate', 0)
        self._addNumberProperty('totalVehiclesCount', 0)
        self._addArrayProperty('vehicles', Array())
        self.onGoBack = self._addCommand('onGoBack')
        self.onShowVehicle = self._addCommand('onShowVehicle')
        self.onCompareVehicle = self._addCommand('onCompareVehicle')
        self.onResetFilter = self._addCommand('onResetFilter')