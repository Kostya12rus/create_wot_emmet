# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/visual_script/vehicle_blocks.py
from block import Block, Meta
from slot_types import SLOT_TYPE
import items.vehicles as vehicles

class VehicleMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 16738047

    @classmethod
    def blockCategory(cls):
        return 'Vehicle'

    @classmethod
    def blockIcon(cls):
        return ':vse/blocks/tank'


class VehicleEventsMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 16738047

    @classmethod
    def blockCategory(cls):
        return 'Vehicle'

    @classmethod
    def blockIcon(cls):
        return ':vse/blocks/arena_event'


class GetVehicleId(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(GetVehicleId, self).__init__(*args, **kwargs)
        self._vehicle = self._makeDataInputSlot('vehicle', SLOT_TYPE.VEHICLE)
        self._res = self._makeDataOutputSlot('id', SLOT_TYPE.INT, self._exec)

    def _exec(self):
        vehicle = self._vehicle.getValue()
        if vehicle:
            self._res.setValue(vehicle.id)