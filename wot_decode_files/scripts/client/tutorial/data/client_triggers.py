# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/data/client_triggers.py
import logging
from gui.Scaleform.genConsts.TUTORIAL_TRIGGER_TYPES import TUTORIAL_TRIGGER_TYPES
_logger = logging.getLogger(__name__)
_COMPONENT_STATE_TRIGGERS = {'visible': TUTORIAL_TRIGGER_TYPES.VISIBLE_CHANGE, 
   'enabled': TUTORIAL_TRIGGER_TYPES.ENABLED_CHANGE}

class _ComponentState(object):

    def __init__(self):
        self.__previousState = False
        self.__actualState = False

    def getActualState(self):
        return self.__actualState

    def updateState(self, newState):
        self.__previousState = self.__actualState
        self.__actualState = newState

    def isStateChanged(self):
        return self.__previousState is not self.__actualState


class ClientTriggers(object):

    def __init__(self):
        self.__hintNeededStates = {}
        self.__hintRealStates = {}
        self.__activeHints = set()

    def clear(self):
        self.__hintNeededStates = None
        self.__hintRealStates = None
        self.__activeHints = None
        return

    def setStates(self, hints):
        for items in hints.values():
            for item in items:
                itemID = item['itemID']
                triggers = item['checked-ui-state']
                if triggers:
                    states = {trigger.state: trigger.value for trigger in triggers}
                    self.__hintNeededStates[itemID] = states

        for itemID, realStates in self.__hintNeededStates.iteritems():
            defaultStates = {state: _ComponentState() for state in realStates.keys()}
            self.__hintRealStates[itemID] = defaultStates

    def getNeededStates(self):
        return self.__hintNeededStates

    def addActiveHint(self, itemID):
        self.__activeHints.add(itemID)

    def removeActiveHint(self, itemID):
        if itemID in self.__activeHints:
            self.__activeHints.remove(itemID)

    def removeActiveHints(self):
        self.__activeHints.clear()

    def getNeededTriggersForComponent(self, itemID):
        triggers = []
        if itemID not in self.__hintNeededStates:
            return triggers
        states = self.__hintNeededStates[itemID].keys()
        if states:
            triggers = [ _COMPONENT_STATE_TRIGGERS[state] for state in states ]
        return triggers

    def updateRealState(self, itemID, state=None, newStateValue=None):
        if itemID not in self.__hintRealStates:
            return
        else:
            if state is None:
                for _ in self.__hintRealStates[itemID].keys():
                    self.__hintRealStates[itemID][state] = _ComponentState()

                return
            if state not in self.__hintRealStates[itemID]:
                return
            self.__hintRealStates[itemID][state].updateState(newStateValue)
            return

    def checkState(self, itemID):
        if itemID not in self.__hintNeededStates:
            return True
        for state, value in self.__hintNeededStates[itemID].iteritems():
            if value != self.__hintRealStates[itemID][state].getActualState():
                return False

        return True

    def isStateChanged(self, itemID, state):
        return self.__hintRealStates[itemID][state].isStateChanged()