# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/resource_well/award_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class AwardViewModel(ViewModel):
    __slots__ = ('showInHangar', )

    def __init__(self, properties=2, commands=1):
        super(AwardViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getPersonalNumber(self):
        return self._getString(1)

    def setPersonalNumber(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(AwardViewModel, self)._initialize()
        self._addViewModelProperty('vehicleInfo', VehicleInfoModel())
        self._addStringProperty('personalNumber', '')
        self.showInHangar = self._addCommand('showInHangar')