# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/turret_gun_angles.py
from gui.ClientHangarSpace import hangarCFG
from skeletons.gui.turret_gun_angles import ITurretAndGunAngles

class TurretAndGunAngles(ITurretAndGunAngles):

    def __init__(self):
        self.__gunPitch = 0.0
        self.__turretYaw = 0.0

    def init(self):
        self.reset()

    def reset(self):
        cfg = hangarCFG()
        self.__gunPitch = cfg.get('vehicle_gun_pitch', 0.0)
        self.__turretYaw = cfg.get('vehicle_turret_yaw', 0.0)

    def destroy(self):
        self.__gunPitch = 0.0
        self.__turretYaw = 0.0

    def set(self, gunPitch=0.0, turretYaw=0.0):
        self.__gunPitch = gunPitch
        self.__turretYaw = turretYaw

    def getTurretYaw(self):
        return self.__turretYaw

    def getGunPitch(self):
        return self.__gunPitch