# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicle_systems/components/siegeEffectsController.py
import Math, cgf_obsolete_script.py_component
from constants import VEHICLE_SIEGE_STATE

class SiegeEffectsController(cgf_obsolete_script.py_component.Component):
    SIEGE_TIMEOUT = 0.5
    SIEGE_IMPULSE = 0.1
    HIGH_PRIORITY_TICK_RATE = 0.1
    NPC_TICK_RATE = 0.25

    def __init__(self, appearance, isHighPriority):
        self.__appearance = appearance
        self.__effectManager = appearance.customEffectManager
        self.__siegeTimeOut = 0.0
        self.__siegeInProgress = 0
        self.__state = VEHICLE_SIEGE_STATE.DISABLED
        if isHighPriority:
            self.__tickRate = SiegeEffectsController.HIGH_PRIORITY_TICK_RATE
        else:
            self.__tickRate = SiegeEffectsController.NPC_TICK_RATE

    def destroy(self):
        self.__effectManager = None
        self.__appearance = None
        return

    def __shake(self):
        matrix = Math.Matrix(self.__appearance.compoundModel.matrix)
        impulseDir = -matrix.applyToAxis(2)
        self.__appearance.receiveShotImpulse(impulseDir, self.SIEGE_IMPULSE)

    def onSiegeStateChanged(self, newState, timeToNextMode):
        switchingTime = timeToNextMode if timeToNextMode > 0.0 else self.SIEGE_TIMEOUT
        if self.__state != newState:
            if newState == VEHICLE_SIEGE_STATE.SWITCHING_ON:
                self.__siegeInProgress = 1
                self.__siegeTimeOut = switchingTime
                self.__shake()
            elif newState == VEHICLE_SIEGE_STATE.ENABLED:
                self.__siegeInProgress = 0
            elif newState == VEHICLE_SIEGE_STATE.SWITCHING_OFF:
                self.__siegeInProgress = 1
                self.__siegeTimeOut = switchingTime
                self.__shake()
            elif newState == VEHICLE_SIEGE_STATE.DISABLED:
                self.__siegeInProgress = 0
            self.__state = newState

    def tick(self):
        if self.__siegeTimeOut > 0.0:
            self.__siegeTimeOut -= self.__tickRate
        self.__effectManager.variables['siegeStart'] = 1 if self.__siegeTimeOut > 0.0 else 0
        self.__effectManager.variables['siegeProgress'] = self.__siegeInProgress
        return self.__tickRate