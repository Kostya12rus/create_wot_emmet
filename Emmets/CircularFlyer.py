# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/CircularFlyer.py
import math, BigWorld, AnimationSequence
from Math import Matrix, Vector3
from debug_utils import LOG_CURRENT_EXCEPTION
from vehicle_systems.stricted_loading import makeCallbackWeak
import SoundGroups

class CircularFlyer(BigWorld.UserDataObject):

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        self.__prevTime = BigWorld.time()
        self.__angularVelocity = 2 * math.pi / self.rotationPeriod
        if not self.rotateClockwise:
            self.__angularVelocity *= -1
        self.__currentAngle = 0.0
        self.__updateCallbackId = None
        self.__model = None
        self.__modelMatrix = None
        self.__sound = None
        self.__animator = None
        BigWorld.loadResourceListBG((self.modelName, self.pixieName), makeCallbackWeak(self.__onResourcesLoaded))
        return

    def __del__(self):
        self.__clear()

    def __clear(self):
        if self.__updateCallbackId is not None:
            BigWorld.cancelCallback(self.__updateCallbackId)
        self.__updateCallbackId = None
        if self.__sound is not None:
            self.__sound.stop()
            self.__sound.releaseMatrix()
            self.__sound = None
        if self.__model is not None:
            self.__animator = None
            BigWorld.delModel(self.__model)
            self.__model = None
        return

    def __onResourcesLoaded(self, resourceRefs):
        if self.guid not in BigWorld.userDataObjects:
            return
        else:
            self.__clear()
            if self.modelName in resourceRefs.failedIDs:
                return
            try:
                self.__model = resourceRefs[self.modelName]
                self.__modelMatrix = Matrix()
                self.__modelMatrix.setIdentity()
                servo = BigWorld.Servo(self.__modelMatrix)
                self.__model.addMotor(servo)
                BigWorld.addModel(self.__model)
                if self.actionName != '':
                    clipResource = self.__model.deprecatedGetAnimationClipResource(self.actionName)
                    if clipResource:
                        spaceID = BigWorld.player().spaceID
                        loader = AnimationSequence.Loader(clipResource, spaceID)
                        animator = loader.loadSync()
                        animator.bindTo(AnimationSequence.ModelWrapperContainer(self.__model, spaceID))
                        animator.start()
                        self.__animator = animator
                if self.pixieName != '' and self.pixieName not in resourceRefs.failedIDs:
                    pixieNode = self.__model.node(self.pixieHardPoint)
                    pixieNode.attach(resourceRefs[self.pixieName])
                if self.soundName != '':
                    self.__sound = SoundGroups.g_instance.getSound3D(self.__modelMatrix, self.soundName)
            except Exception:
                LOG_CURRENT_EXCEPTION()
                self.__model = None
                return

            self.__prevTime = BigWorld.time()
            self.__update()
            return

    def __update(self):
        self.__updateCallbackId = None
        self.__updateCallbackId = BigWorld.callback(0.0, self.__update)
        curTime = BigWorld.time()
        dt = curTime - self.__prevTime
        self.__prevTime = curTime
        self.__currentAngle += self.__angularVelocity * dt
        if self.__currentAngle > 2 * math.pi:
            self.__currentAngle -= 2 * math.pi
        elif self.__currentAngle < -2 * math.pi:
            self.__currentAngle += 2 * math.pi
        radialPosition = Vector3(self.radius * math.sin(self.__currentAngle), 0, self.radius * math.cos(self.__currentAngle))
        modelYaw = self.__currentAngle
        if self.rotateClockwise:
            modelYaw += math.pi / 2
        else:
            modelYaw -= math.pi / 2
        localMatrix = Matrix()
        localMatrix.setRotateY(modelYaw)
        localMatrix.translation = radialPosition
        self.__modelMatrix.setRotateYPR((self.yaw, self.pitch, self.roll))
        self.__modelMatrix.translation = self.position
        self.__modelMatrix.preMultiply(localMatrix)
        return