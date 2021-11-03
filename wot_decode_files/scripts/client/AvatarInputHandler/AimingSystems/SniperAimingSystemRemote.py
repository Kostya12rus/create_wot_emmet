# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/AimingSystems/SniperAimingSystemRemote.py
import BigWorld
from AvatarInputHandler.subfilters_constants import AVATAR_SUBFILTERS
from AvatarInputHandler.AimingSystems.SniperAimingSystem import SniperAimingSystem

class SniperAimingSystemRemote(SniperAimingSystem):

    def handleMovement(self, dx, dy):
        pass

    def update(self, deltaTime):
        super(SniperAimingSystemRemote, self).update(deltaTime)
        player = BigWorld.player()
        shotPoint = player.remoteCamera.shotPoint
        getVector3 = getattr(player.filter, 'getVector3', None)
        if getVector3 is not None:
            shotPoint = getVector3(AVATAR_SUBFILTERS.CAMERA_SHOT_POINT, BigWorld.serverTime())
        self.focusOnPos(shotPoint)
        super(SniperAimingSystemRemote, self).overrideZoom(float(player.remoteCamera.zoom))
        return

    def overrideZoom(self, zoom):
        return self.getZoom()

    def enable(self, *args):
        super(SniperAimingSystemRemote, self).enable(*args)
        vehicle = BigWorld.player().getVehicleAttached()
        if vehicle is not None:
            vehicle.filter.enableStabilisedMatrix(True)
        return

    def disable(self):
        super(SniperAimingSystemRemote, self).disable()
        vehicle = BigWorld.player().getVehicleAttached()
        if vehicle is not None:
            vehicle.filter.enableStabilisedMatrix(False)
        return