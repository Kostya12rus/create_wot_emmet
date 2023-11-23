# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/slot_vehicle_info_model.py
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class SlotVehicleInfoModel(VehicleInfoModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(SlotVehicleInfoModel, self).__init__(properties=properties, commands=commands)

    def getVehicleID(self):
        return self._getNumber(8)

    def setVehicleID(self, value):
        self._setNumber(8, value)

    def _initialize(self):
        super(SlotVehicleInfoModel, self)._initialize()
        self._addNumberProperty('vehicleID', 0)