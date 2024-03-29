# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/DynamicCameras/DualGunCamera.py
import BigWorld
from BigWorld import DualGunAimingSystem, DualGunAimingSystemRemote
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