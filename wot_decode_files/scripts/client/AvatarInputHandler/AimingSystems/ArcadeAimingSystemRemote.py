# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/AimingSystems/ArcadeAimingSystemRemote.py
import BigWorld
from AvatarInputHandler.subfilters_constants import AVATAR_SUBFILTERS
from AvatarInputHandler.AimingSystems.ArcadeAimingSystem import ArcadeAimingSystem

class ArcadeAimingSystemRemote(ArcadeAimingSystem):

    def handleMovement(self, dx, dy):
        if not BigWorld.player().isObserverFPV:
            super(ArcadeAimingSystemRemote, self).handleMovement(dx, dy)

    def update(self, deltaTime):
        super(ArcadeAimingSystemRemote, self).update(deltaTime)
        player = BigWorld.player()
        if player.isObserverFPV:
            shotPoint = player.remoteCamera.shotPoint
            zoom = player.remoteCamera.zoom
            getVector3 = getattr(player.filter, 'getVector3', None)
            if getVector3 is not None:
                shotPoint = getVector3(AVATAR_SUBFILTERS.CAMERA_SHOT_POINT, BigWorld.serverTime())
            self.focusOnPos(shotPoint)
            self.distanceFromFocus = zoom
        return