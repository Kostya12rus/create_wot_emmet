# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/DynamicCameras/OnlyArtyCamera.py
import BigWorld
from AvatarInputHandler.DynamicCameras.ArtyCamera import ArtyCamera

def getCameraAsSettingsHolder(settingsDataSec):
    return OnlyArtyCamera(settingsDataSec)


class OnlyArtyCamera(ArtyCamera):

    @staticmethod
    def _createAimingSystem():
        from BigWorld import OnlyArtyAimingSystemRemote, OnlyArtyAimingSystem
        if BigWorld.player().isObserver():
            return OnlyArtyAimingSystemRemote(BigWorld.player().getVehicleDescriptor().shot.maxDistance)
        return OnlyArtyAimingSystem(BigWorld.player().getVehicleDescriptor().shot.maxDistance)

    def setMaxDistance(self, newMaxDist):
        self._aimingSystem.setMaxRadius(newMaxDist)