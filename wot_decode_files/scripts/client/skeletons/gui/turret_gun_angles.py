# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/turret_gun_angles.py


class ITurretAndGunAngles(object):

    def init(self):
        raise NotImplementedError

    def destroy(self):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    def set(self, gunPitch=0.0, turretYaw=0.0):
        raise NotImplementedError

    def getGunPitch(self):
        raise NotImplementedError

    def getTurretYaw(self):
        raise NotImplementedError