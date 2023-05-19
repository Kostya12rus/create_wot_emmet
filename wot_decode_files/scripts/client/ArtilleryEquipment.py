# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/ArtilleryEquipment.py
import math_utils, BigWorld

class ArtilleryEquipment(BigWorld.UserDataObject):
    launchVelocity = property((lambda self: self.__launchVelocity))

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        launchDir = math_utils.createRotationMatrix((self.__dict__['yaw'], self.__dict__['pitch'], 0)).applyToAxis(2)
        launchDir.normalise()
        self.__launchVelocity = launchDir * self.speed