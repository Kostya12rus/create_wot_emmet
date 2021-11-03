# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/visual_script/vehicle_blocks.py
from block import Block, Meta
from slot_types import SLOT_TYPE
from visual_script.dependency import dependencyImporter
from visual_script.misc import errorVScript
vehicles, = dependencyImporter('items.vehicles')

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


class VehicleClass(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(VehicleClass, self).__init__(*args, **kwargs)
        self._vehicle = self._makeDataInputSlot('vehicle', SLOT_TYPE.VEHICLE)
        self._className = self._makeDataOutputSlot('className', SLOT_TYPE.STR, self._getClassName)

    def _getClassName(self):
        className = ''
        if self._vehicle.hasValue() and self._vehicle.getValue() is not None:
            className = vehicles.getVehicleClass(self._vehicle.getValue().typeDescriptor.type.compactDescr)
        if className is None:
            errorVScript(self, 'Unknown vehicle className')
        self._className.setValue(className)
        return