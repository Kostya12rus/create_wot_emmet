# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/data/bootcamp/effects.py
from tutorial.data.effects import EFFECT_TYPE, SimpleEffect, HasTargetEffect

class RequestExclusiveHintEffect(HasTargetEffect):

    def __init__(self, componentID, soundID, conditions=None):
        super(RequestExclusiveHintEffect, self).__init__(componentID, EFFECT_TYPE.REQUEST_EXCLUSIVE_HINT, conditions=conditions)
        self.__soundID = soundID

    def getSoundID(self):
        return self.__soundID


class StartVSEPlanEffect(SimpleEffect):

    def __init__(self, plan, conditions=None):
        super(StartVSEPlanEffect, self).__init__(EFFECT_TYPE.START_VSE_PLAN, conditions=conditions)
        self.__plan = plan

    def getPlan(self):
        return self.__plan