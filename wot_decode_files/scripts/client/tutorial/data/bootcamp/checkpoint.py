# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/data/bootcamp/checkpoint.py
from tutorial.data.has_id import HasID

class Checkpoint(HasID):

    def __init__(self, entityID, conditions, effects):
        super(Checkpoint, self).__init__(entityID=entityID)
        self.__conditions = conditions
        self.__effects = effects

    def getConditions(self):
        return self.__conditions

    def getEffects(self):
        return self.__effects[:]