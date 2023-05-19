# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/DynamicCameras/FlameArtyCamera.py
import BigWorld
from AvatarInputHandler.DynamicCameras.ArtyCamera import ArtyCamera

def getCameraAsSettingsHolder(settingsDataSec):
    return FlameArtyCamera(settingsDataSec)


class FlameArtyCamera(ArtyCamera):

    @staticmethod
    def _createAimingSystem():
        from BigWorld import FlameArtyAimingSystemRemote, FlameArtyAimingSystem
        if BigWorld.player().isObserver():
            return FlameArtyAimingSystemRemote(BigWorld.player().getVehicleDescriptor().shot.maxDistance)
        return FlameArtyAimingSystem(BigWorld.player().getVehicleDescriptor().shot.maxDistance)

    def setMaxDistance(self, newMaxDist):
        self._aimingSystem.setMaxRadius(newMaxDist)