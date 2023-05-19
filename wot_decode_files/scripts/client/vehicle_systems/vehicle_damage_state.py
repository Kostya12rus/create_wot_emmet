# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicle_systems/vehicle_damage_state.py
import constants

class VehicleDamageState(object):
    MODEL_STATE_NAMES = ('undamaged', 'destroyed', 'exploded')
    __healthToStateMap = {0: 'destruction', 
       constants.SPECIAL_VEHICLE_HEALTH.AMMO_BAY_DESTROYED: 'ammoBayBurnOff', 
       constants.SPECIAL_VEHICLE_HEALTH.TURRET_DETACHED: 'ammoBayExplosion', 
       constants.SPECIAL_VEHICLE_HEALTH.FUEL_EXPLODED: 'fuelExplosion', 
       constants.SPECIAL_VEHICLE_HEALTH.DESTR_BY_FALL_RAMMING: 'rammingDestruction'}

    @staticmethod
    def getState(health, isCrewActive, isUnderWater):
        if health > 0:
            if not isCrewActive:
                if isUnderWater:
                    return 'submersionDeath'
                return 'crewDeath'
            return 'alive'
        return VehicleDamageState.__healthToStateMap[health]

    __stateToModelEffectsMap = {'ammoBayExplosion': ('exploded', None), 
       'ammoBayBurnOff': ('destroyed', None), 
       'fuelExplosion': ('destroyed', 'fuelExplosion'), 
       'destruction': ('destroyed', 'destruction'), 
       'crewDeath': ('undamaged', 'crewDeath'), 
       'rammingDestruction': ('destroyed', 'rammingDestruction'), 
       'submersionDeath': ('undamaged', 'submersionDeath'), 
       'alive': ('undamaged', 'empty')}

    @staticmethod
    def getStateParams(state):
        return VehicleDamageState.__stateToModelEffectsMap[state]

    state = property((lambda self: self.__state))
    modelState = property((lambda self: self.__model))
    isCurrentModelDamaged = property((lambda self: VehicleDamageState.isDamagedModel(self.modelState)))
    isCurrentModelUndamaged = property((lambda self: VehicleDamageState.isUndamagedModel(self.modelState)))
    isCurrentModelExploded = property((lambda self: VehicleDamageState.isExplodedModel(self.modelState)))
    effect = property((lambda self: self.__effect))

    @staticmethod
    def isDamagedModel(model):
        return model != 'undamaged'

    @staticmethod
    def isUndamagedModel(model):
        return model == 'undamaged'

    @staticmethod
    def isExplodedModel(model):
        return model == 'exploded'

    def __init__(self):
        self.__state = None
        self.__model = None
        self.__effect = None
        return

    def update(self, health, isCrewActive, isUnderWater):
        self.__state = VehicleDamageState.getState(health, isCrewActive, isUnderWater)
        params = VehicleDamageState.getStateParams(self.__state)
        self.__model, self.__effect = params