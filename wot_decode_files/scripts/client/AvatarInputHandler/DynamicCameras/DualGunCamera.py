# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/DynamicCameras/DualGunCamera.py
import BigWorld
from AvatarInputHandler.AimingSystems.DualGunAimingSystem import DualGunAimingSystem
from AvatarInputHandler.AimingSystems.DualGunAimingSystemRemote import DualGunAimingSystemRemote
from AvatarInputHandler.DynamicCameras.SniperCamera import SniperCamera

def getCameraAsSettingsHolder(settingsDataSec):
    return DualGunCamera(settingsDataSec)


class DualGunCamera(SniperCamera):

    def _aimingSystemClass(self):
        if BigWorld.player().isObserver():
            return DualGunAimingSystemRemote
        return DualGunAimingSystem

    def _readCfg(self, dataSec):
        super(DualGunCamera, self)._readCfg(dataSec)
        transitionTime = dataSec.readFloat('transitionTime', 0.3)
        DualGunAimingSystem.setTransitionTime(transitionTime)
        transitionDelay = dataSec.readFloat('transitionDelay', 0.0)
        DualGunAimingSystem.setTransitionDelay(transitionDelay)