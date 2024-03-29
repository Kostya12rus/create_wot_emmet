# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/elite_window/elite_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class EliteViewModel(ViewModel):
    __slots__ = ('onGoToPostProgression', 'onClose')

    def __init__(self, properties=2, commands=2):
        super(EliteViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getIsPostProgressionExists(self):
        return self._getBool(1)

    def setIsPostProgressionExists(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(EliteViewModel, self)._initialize()
        self._addViewModelProperty('vehicleInfo', VehicleInfoModel())
        self._addBoolProperty('isPostProgressionExists', False)
        self.onGoToPostProgression = self._addCommand('onGoToPostProgression')
        self.onClose = self._addCommand('onClose')