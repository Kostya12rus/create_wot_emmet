# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle_royale/tech_parameters_cmp_view_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.battle_royale.br_vehicle_specifications_model import BrVehicleSpecificationsModel

class TechParametersCmpViewModel(ViewModel):
    __slots__ = ('onModulesBtnClick', 'onResized')

    def __init__(self, properties=2, commands=2):
        super(TechParametersCmpViewModel, self).__init__(properties=properties, commands=commands)

    def getVehicleGoodSpec(self):
        return self._getArray(0)

    def setVehicleGoodSpec(self, value):
        self._setArray(0, value)

    @staticmethod
    def getVehicleGoodSpecType():
        return BrVehicleSpecificationsModel

    def getVehicleBadSpec(self):
        return self._getArray(1)

    def setVehicleBadSpec(self, value):
        self._setArray(1, value)

    @staticmethod
    def getVehicleBadSpecType():
        return BrVehicleSpecificationsModel

    def _initialize(self):
        super(TechParametersCmpViewModel, self)._initialize()
        self._addArrayProperty('vehicleGoodSpec', Array())
        self._addArrayProperty('vehicleBadSpec', Array())
        self.onModulesBtnClick = self._addCommand('onModulesBtnClick')
        self.onResized = self._addCommand('onResized')