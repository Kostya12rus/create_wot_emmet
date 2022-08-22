# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/ArtilleryEquipment.py
import math_utils, BigWorld

class ArtilleryEquipment(BigWorld.UserDataObject):
    launchVelocity = property(lambda self: self.__launchVelocity)

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        launchDir = math_utils.createRotationMatrix((self.__dict__['yaw'], self.__dict__['pitch'], 0)).applyToAxis(2)
        launchDir.normalise()
        self.__launchVelocity = launchDir * self.speed