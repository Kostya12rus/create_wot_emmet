# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicle_systems/components/hull_aiming_controller.py
import cgf_obsolete_script.py_component
from constants import VEHICLE_SIEGE_STATE

class HullAimingController(cgf_obsolete_script.py_component.Component):

    def __init__(self):
        self.__vehicleFilter = None
        self.__vehicleDescriptor = None
        return

    def deactivate(self):
        self.__vehicleFilter = None
        self.__vehicleDescriptor = None
        super(HullAimingController, self).deactivate()
        return

    def destroy(self):
        self.__vehicleFilter = None
        self.__vehicleDescriptor = None
        return

    def setData(self, vehicleFilter, vehicleDescriptor):
        self.__vehicleFilter = vehicleFilter
        self.__vehicleDescriptor = vehicleDescriptor

    def onSiegeStateChanged(self, newState):
        if self.__vehicleFilter is None or self.__vehicleDescriptor is None:
            return
        needUpdateSpringsLength = newState == VEHICLE_SIEGE_STATE.ENABLED or newState == VEHICLE_SIEGE_STATE.DISABLED
        physics = self.__vehicleFilter.getVehiclePhysics()
        if physics is None or not needUpdateSpringsLength:
            return
        newSuspensionSpringLength = self.__vehicleDescriptor.chassis.suspensionSpringsLength
        if newSuspensionSpringLength is not None:
            physics.setDamperSpringsLength(newSuspensionSpringLength['left'], newSuspensionSpringLength['right'])
        return