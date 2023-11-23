# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/tankman_model.py
from frameworks.wulf import ViewModel

class TankmanModel(ViewModel):
    __slots__ = ()
    RECEIVED = 'received'
    FREE = 'free'
    PAID = 'paid'
    IN_SHOP = 'inShop'
    QUEST_CHAIN = 'questChain'
    NOT_FULL = 'notFull'
    AVAILABLE_IN_QUEST_CHAIN = 'availableInQuestChain'
    UNAVAILABLE = 'unavailable'

    def __init__(self, properties=7, commands=0):
        super(TankmanModel, self).__init__(properties=properties, commands=commands)

    def getFullName(self):
        return self._getString(0)

    def setFullName(self, value):
        self._setString(0, value)

    def getGroupName(self):
        return self._getString(1)

    def setGroupName(self, value):
        self._setString(1, value)

    def getState(self):
        return self._getString(2)

    def setState(self, value):
        self._setString(2, value)

    def getChapterID(self):
        return self._getNumber(3)

    def setChapterID(self, value):
        self._setNumber(3, value)

    def getProgressionLevel(self):
        return self._getNumber(4)

    def setProgressionLevel(self, value):
        self._setNumber(4, value)

    def getCount(self):
        return self._getNumber(5)

    def setCount(self, value):
        self._setNumber(5, value)

    def getAvailableCount(self):
        return self._getNumber(6)

    def setAvailableCount(self, value):
        self._setNumber(6, value)

    def _initialize(self):
        super(TankmanModel, self)._initialize()
        self._addStringProperty('fullName', '')
        self._addStringProperty('groupName', '')
        self._addStringProperty('state', 'unavailable')
        self._addNumberProperty('chapterID', 0)
        self._addNumberProperty('progressionLevel', 0)
        self._addNumberProperty('count', 1)
        self._addNumberProperty('availableCount', 0)