# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/bootcamp/bootcamp_final_reward_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.bootcamp.vehicle_model import VehicleModel

class BootcampFinalRewardModel(ViewModel):
    __slots__ = ('onProceed', )

    def __init__(self, properties=2, commands=1):
        super(BootcampFinalRewardModel, self).__init__(properties=properties, commands=commands)

    def getIsNeedAwarding(self):
        return self._getBool(0)

    def setIsNeedAwarding(self, value):
        self._setBool(0, value)

    def getVehicles(self):
        return self._getArray(1)

    def setVehicles(self, value):
        self._setArray(1, value)

    @staticmethod
    def getVehiclesType():
        return VehicleModel

    def _initialize(self):
        super(BootcampFinalRewardModel, self)._initialize()
        self._addBoolProperty('isNeedAwarding', False)
        self._addArrayProperty('vehicles', Array())
        self.onProceed = self._addCommand('onProceed')