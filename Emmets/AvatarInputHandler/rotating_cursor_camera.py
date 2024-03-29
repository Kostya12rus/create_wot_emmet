# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/rotating_cursor_camera.py
import math, BigWorld, math_utils

class RotatingCoursorCamera(object):

    def __init__(self, cfg):
        self.__camera = None
        self.__minPitch, self.__maxPitch = cfg.readVector2('pitchLimits')
        self.__minDist, self.__maxDist = cfg.readVector2('distanceLimits')
        self.__sensitivity = cfg.readFloat('sensitivity')
        self.__maxDistHalfLife = cfg.readFloat('maxDistHalfLife', 0.0)
        self.__pivotOffset = cfg.readVector3('pivotOffset')
        return

    @property
    def sourceMatrix(self):
        return self.__camera.source

    @property
    def pivotDistance(self):
        return self.__camera.pivotMaxDist

    def setup(self, targetPosition, initialRotations, distanceToTarget):
        if not self.__camera:
            self.__createCamera()
        self.__camera.pivotMaxDist = self.clampDistance(distanceToTarget)
        self.__camera.target = math_utils.createTranslationMatrix(targetPosition)
        self.__camera.source = initialRotations
        self.__camera.forceUpdate()

    def move(self, rotations, distance):
        if self.__camera is None:
            return
        else:
            self.__camera.source = rotations
            self.__camera.pivotMaxDist = distance
            self.__camera.forceUpdate()
            return

    def destroy(self):
        self.__camera = None
        return

    def handleMouseEvent(self, dx, dy, dz):
        currYaw, currPitch = self.__camera.source.yaw, self.__camera.source.pitch
        newYaw = (currYaw + math.radians(dx * self.__sensitivity)) % (2 * math.pi)
        newPitch = currPitch + math.radians(-dy * self.__sensitivity)
        newPitch = math_utils.clamp(-self.__maxPitch, -self.__minPitch, newPitch)
        self.__camera.source = math_utils.createRotationMatrix((newYaw, newPitch, 0))
        self.__camera.pivotMaxDist = self.clampDistance(self.__camera.pivotMaxDist - dz)
        self.__camera.forceUpdate()

    def clampDistance(self, value):
        return math_utils.clamp(self.__minDist, self.__maxDist, value)

    def __createCamera(self):
        self.__camera = BigWorld.CursorCamera()
        self.__camera.maxDistHalfLife = self.__maxDistHalfLife
        self.__camera.pivotPosition = self.__pivotOffset
        BigWorld.camera(self.__camera)