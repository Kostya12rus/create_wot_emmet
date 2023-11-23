# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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