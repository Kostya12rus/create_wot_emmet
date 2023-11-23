# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/visual_script_client/contexts/vehicle_context.py
import weakref
from visual_script.context import VScriptContext, vse_get_property
from visual_script.misc import ASPECT
from visual_script.slot_types import SLOT_TYPE

class VehicleContextClient(VScriptContext):

    def __init__(self, vehicle):
        super(VehicleContextClient, self).__init__(ASPECT.CLIENT)
        self._vehicle = vehicle

    def destroy(self):
        super(VehicleContextClient, self).destroy()
        self._vehicle = None
        return

    @vse_get_property(SLOT_TYPE.VEHICLE, display_name='Self', description='Return instance of current vehicle', aspects=[
     ASPECT.CLIENT])
    def getSelf(self):
        return weakref.proxy(self._vehicle)