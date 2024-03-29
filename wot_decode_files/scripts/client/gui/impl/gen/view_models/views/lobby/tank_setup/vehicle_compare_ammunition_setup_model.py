# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/vehicle_compare_ammunition_setup_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.tank_setup.main_tank_setup_model import MainTankSetupModel

class VehicleCompareAmmunitionSetupModel(ViewModel):
    __slots__ = ('onClose', 'onResized', 'onViewRendered', 'onAnimationEnd')

    def __init__(self, properties=4, commands=4):
        super(VehicleCompareAmmunitionSetupModel, self).__init__(properties=properties, commands=commands)

    @property
    def tankSetup(self):
        return self._getViewModel(0)

    @staticmethod
    def getTankSetupType():
        return MainTankSetupModel

    @property
    def vehicleInfo(self):
        return self._getViewModel(1)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getShow(self):
        return self._getBool(2)

    def setShow(self, value):
        self._setBool(2, value)

    def getSelectedSlot(self):
        return self._getNumber(3)

    def setSelectedSlot(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(VehicleCompareAmmunitionSetupModel, self)._initialize()
        self._addViewModelProperty('tankSetup', MainTankSetupModel())
        self._addViewModelProperty('vehicleInfo', VehicleInfoModel())
        self._addBoolProperty('show', False)
        self._addNumberProperty('selectedSlot', -1)
        self.onClose = self._addCommand('onClose')
        self.onResized = self._addCommand('onResized')
        self.onViewRendered = self._addCommand('onViewRendered')
        self.onAnimationEnd = self._addCommand('onAnimationEnd')