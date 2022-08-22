# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/linkedset.py


class ILinkedSetController(object):
    onStateChanged = None

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def isLinkedSetEnabled(self):
        raise NotImplementedError

    def isLinkedSetFinished(self):
        raise NotImplementedError

    def hasLinkedSetFinishToken(self):
        raise NotImplementedError

    def isFinalQuest(self, quest):
        raise NotImplementedError

    def getFinalQuest(self):
        raise NotImplementedError

    def getMaxMissionID(self):
        raise NotImplementedError

    def getCompletedButNotShowedQuests(self):
        raise NotImplementedError

    def getMissions(self):
        raise NotImplementedError

    def getMissionByID(self, missionID):
        raise NotImplementedError

    def isBootcampQuest(self, quest):
        raise NotImplementedError

    def isLinkedSetQuest(self, questID):
        raise NotImplementedError

    def isLinkedSetQuestWithAwards(self, questID):
        raise NotImplementedError

    def getInitialMissionID(self):
        raise NotImplementedError

    def getBonusForBootcampMission(self):
        raise NotImplementedError

    def getCompletedLinkedSetQuests(self, filterFunc=None):
        raise NotImplementedError

    def getLinkedSetQuests(self, filterFunc=None):
        raise NotImplementedError

    def showAwardView(self, questIDs):
        raise NotImplementedError