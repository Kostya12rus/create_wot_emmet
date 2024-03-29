# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/FlockExotic.py
import math, random
from functools import partial
import BigWorld, Math, AnimationSequence, FlockManager
from Flock import FlockLike
from helpers.CallbackDelayer import CallbackDelayer
from debug_utils import LOG_CURRENT_EXCEPTION, LOG_ERROR
_MATH_2PI = math.pi * 2.0

class FlockExotic(BigWorld.Entity, FlockLike, CallbackDelayer):

    def __init__(self):
        BigWorld.Entity.__init__(self)
        FlockLike.__init__(self)
        CallbackDelayer.__init__(self)
        self.flightAngleMin = math.radians(self.flightAngleMin)
        self.flightAngleMax = math.radians(self.flightAngleMax)
        if self.flightAngleMax < self.flightAngleMin:
            self.flightAngleMax, self.flightAngleMin = self.flightAngleMin, self.flightAngleMax
        if self.flightAngleMax - self.flightAngleMin > _MATH_2PI:
            LOG_ERROR('flightAngleMax or  flightAngleMin have incorrect values: arc greater than 2*pi')
        self.__isTriggered = False
        self.__models = []

    def prerequisites(self):
        return self._getModelsToLoad()

    def __createMotor(self, positionStart, positionEnd, speed, flightTime):
        time1 = BigWorld.time()
        time2 = time1 + self.accelerationTime
        time3 = time2 + flightTime
        initSpeed = speed * random.uniform(self.initSpeedRandom[0], self.initSpeedRandom[1])
        controlPoint1 = (
         positionStart, initSpeed, time1)
        controlPoint2 = (positionStart + (initSpeed + speed) / 2.0, speed, time2)
        motor = BigWorld.PyTimedWarplaneMotor(controlPoint1, controlPoint2, 0.0)
        motor.addTrajectoryPoint(positionEnd, speed, time3)
        return motor

    def onEnterWorld(self, prereqs):
        self.__loadModels(prereqs)
        FlockManager.getManager().addFlock(self.position, self.triggerRadius, self.explosionRadius, self.respawnTime, self)

    def onLeaveWorld(self):
        self.__removeModels()
        FlockLike.destroy(self)
        self.__models = []
        self.models = []
        CallbackDelayer.destroy(self)

    def name(self):
        return 'FlockExotic'

    def __loadModels(self, prereqs):
        try:
            for modelId in prereqs.keys():
                if modelId in prereqs.failedIDs:
                    LOG_ERROR('Failed to load flock model: %s' % modelId)
                    continue
                model = prereqs[modelId]
                model.moveAttachments = True
                model.visible = False
                self.__models.append(model)
                animSpeed = random.uniform(self.animSpeedMin, self.animSpeedMax)
                clipResource = model.deprecatedGetAnimationClipResource('FlockAnimAction')
                loader = AnimationSequence.Loader(clipResource, self.spaceID)
                animator = loader.loadSync()
                animator.bindTo(AnimationSequence.ModelWrapperContainer(model, self.spaceID))
                animator.speed = animSpeed
                self._animators.append(animator)

        except Exception:
            LOG_CURRENT_EXCEPTION()

    def __removeModels(self):
        for model in self.models:
            self.__removeModel(model)

        self.models = []

    def __removeModel(self, model):
        index = self.__models.index(model)
        if index < len(self._animators):
            self._animators[index].stop()
        self._delSound()
        model.motors = ()
        model.position = self.position
        model.visible = False
        self.delModel(model)

    def __getRandomSpawnPos(self):
        randHeight = random.uniform(0, self.spawnHeight)
        randAngle = random.uniform(0, 2 * math.pi)
        randRadius = random.uniform(0, self.spawnRadius)
        return Math.Vector3(randRadius * math.cos(randAngle), randHeight, randRadius * math.sin(randAngle)) + self.position

    def __getRandomTargetPos(self, startPos):
        randHeight = random.uniform(0, self.flightHeight)
        randAngle = random.uniform(self.flightAngleMin, self.flightAngleMax)
        direction = Math.Vector3(self.flightRadius * math.cos(randAngle), self.flightOffsetFromOrigin + randHeight, self.flightRadius * math.sin(randAngle)) + self.position
        direction = direction - startPos
        direction.normalise()
        direction *= self.speed * self.lifeTime
        return startPos + direction

    def onTrigger(self):
        index = 0
        animatorIndex = 0
        for model in self.__models:
            model.visible = True
            self.addModel(model)
            self._animators[animatorIndex].start()
            animatorIndex += 1
            model.position = self.__getRandomSpawnPos()
            targetPos = self.__getRandomTargetPos(model.position)
            direction = targetPos - model.position
            dirLength = direction.length
            speed = self.speed * random.uniform(self.speedRandom[0], self.speedRandom[1])
            if dirLength > 0.0:
                velocity = direction * speed / dirLength
                velocityLen = velocity.length
                if velocityLen > 0.0:
                    flightTime = dirLength / velocityLen
                    motor = self.__createMotor(model.position, targetPos, velocity, flightTime)
                    model.addMotor(motor)
                    self.delayCallback(flightTime, partial(self.__removeModel, model))
                    if index == 0:
                        self._addSound(model, self.flightSound)
                    index += 1