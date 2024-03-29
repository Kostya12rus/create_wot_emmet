# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/DamagePanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class DamagePanelMeta(BaseDAAPIComponent):

    def clickToTankmanIcon(self, entityName):
        self._printOverrideError('clickToTankmanIcon')

    def clickToDeviceIcon(self, entityName):
        self._printOverrideError('clickToDeviceIcon')

    def clickToFireIcon(self):
        self._printOverrideError('clickToFireIcon')

    def clickToStunTimer(self):
        self._printOverrideError('clickToStunTimer')

    def getTooltipData(self, entityName, state):
        self._printOverrideError('getTooltipData')

    def as_setPlayerInfoS(self, playerName, clanName, regionName, vehicleTypeName):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerInfo(playerName, clanName, regionName, vehicleTypeName)

    def as_setupS(self, healthStr, progress, indicatorType, crewLayout, yawLimits, hasTurretRotator, hasWheel, isAutoRotationOn, hasYoh):
        if self._isDAAPIInited():
            return self.flashObject.as_setup(healthStr, progress, indicatorType, crewLayout, yawLimits, hasTurretRotator, hasWheel, isAutoRotationOn, hasYoh)

    def as_setupWheeledS(self, wheelsCount):
        if self._isDAAPIInited():
            return self.flashObject.as_setupWheeled(wheelsCount)

    def as_updateHealthS(self, healthStr, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_updateHealth(healthStr, progress)

    def as_updateSpeedS(self, speed):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSpeed(speed)

    def as_setCruiseModeS(self, mode):
        if self._isDAAPIInited():
            return self.flashObject.as_setCruiseMode(mode)

    def as_setAutoRotationS(self, isOn):
        if self._isDAAPIInited():
            return self.flashObject.as_setAutoRotation(isOn)

    def as_updateDeviceStateS(self, deviceName, deviceState):
        if self._isDAAPIInited():
            return self.flashObject.as_updateDeviceState(deviceName, deviceState)

    def as_updateRepairingDeviceS(self, deviceName, percents, seconds, repairMode):
        if self._isDAAPIInited():
            return self.flashObject.as_updateRepairingDevice(deviceName, percents, seconds, repairMode)

    def as_setVehicleDestroyedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleDestroyed()

    def as_setCrewDeactivatedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_setCrewDeactivated()

    def as_showS(self, isShow):
        if self._isDAAPIInited():
            return self.flashObject.as_show(isShow)

    def as_setFireInVehicleS(self, isInFire):
        if self._isDAAPIInited():
            return self.flashObject.as_setFireInVehicle(isInFire)

    def as_setStaticDataS(self, fireMsg):
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(fireMsg)

    def as_resetS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_reset()

    def as_setPlaybackSpeedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlaybackSpeed(value)

    def as_showStatusS(self, statusID, time, animated):
        if self._isDAAPIInited():
            return self.flashObject.as_showStatus(statusID, time, animated)

    def as_hideStatusS(self, statusID, animated):
        if self._isDAAPIInited():
            return self.flashObject.as_hideStatus(statusID, animated)

    def as_setStatusTimerSnapshotS(self, statusID, timeLeft):
        if self._isDAAPIInited():
            return self.flashObject.as_setStatusTimerSnapshot(statusID, timeLeft)

    def as_setSpeedModeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSpeedMode(value)

    def as_setRepairTimesVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setRepairTimesVisible(value)