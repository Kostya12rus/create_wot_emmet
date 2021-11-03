# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/GunMarkerComponent.py
import BigWorld

class GunMarkerComponent(BigWorld.DynamicScriptComponent):

    def set_gunMarker(self, _=None):
        gunMarker = self.gunMarker
        if gunMarker is None:
            return
        else:
            avatar = BigWorld.player()
            avatar.updateGunMarker(self.entity.id, gunMarker.gunPosition, gunMarker.shotVector, gunMarker.dispersion)
            return