# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/AimingSystems/ShadowEffect.py
import GUI, math_utils
from constants import DUAL_GUN

class ShadowEffect(object):

    def __init__(self):
        self.__texturePath = 'system/maps/shadow.dds'
        self.__startPositionX = 2.0
        self.__shadowUpInitialPosition = (self.__startPositionX, 0.5, 1.0)
        self.__shadowDownInitialPosition = (self.__startPositionX, -0.5, 1.0)
        self.__size = (3, 1)
        self.__shadowUp = None
        self.__shadowDown = None
        self.cachedPosition = 2.0
        return

    def destroy(self):
        if self.__shadowUp is not None:
            GUI.delRoot(self.__shadowUp)
            self.__shadowUp = None
        if self.__shadowDown is not None:
            GUI.delRoot(self.__shadowDown)
            self.__shadowDown = None
        return

    def __spawnShadow(self, position, path, rotateAngle=None):
        shadow = GUI.Simple(path)
        if rotateAngle is not None:
            shadow.angle = rotateAngle
        shadow.position = position
        shadow.size = self.__size
        shadow.materialFX = GUI.Simple.eMaterialFX.BLEND
        shadow.filterType = GUI.Simple.eFilterType.LINEAR
        shadow.visible = False
        GUI.addRoot(shadow)
        return shadow

    def onGunIndexChanged(self, gunIndex):
        if gunIndex == DUAL_GUN.ACTIVE_GUN.RIGHT:
            self.cachedPosition = self.__startPositionX
        else:
            self.cachedPosition = -self.__startPositionX
        self.move(self.cachedPosition)

    def spawn(self):
        if self.__shadowUp is None or self.__shadowDown is None:
            self.__shadowUp = self.__spawnShadow(self.__shadowUpInitialPosition, self.__texturePath)
            self.__shadowDown = self.__spawnShadow(self.__shadowDownInitialPosition, self.__texturePath, 180)
        return

    def show(self):
        self.__shadowUp.visible = True
        self.__shadowDown.visible = True

    def hide(self):
        self.__shadowUp.visible = False
        self.__shadowDown.visible = False

    def move(self, positionX):
        self.__shadowUp.position[0] = positionX
        self.__shadowDown.position[0] = positionX

    def update(self, coefficient):
        shadowPositionX = round(math_utils.lerp(self.cachedPosition, -self.cachedPosition, coefficient), 1)
        self.move(shadowPositionX)