# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/server_events/settings.py
import time
from contextlib import contextmanager
from account_helpers.AccountSettings import DOG_TAGS, WOT_PLUS, TELECOM_RENTALS
from gui.shared import utils
from helpers import dependency
from skeletons.gui.server_events import IEventsCache

class _PMSettings(utils.SettingRecord):

    def __init__(self, introShown=False, operationsVisited=None, headerAlert=False):
        super(_PMSettings, self).__init__(introShown=introShown, operationsVisited=operationsVisited or set(), headerAlert=headerAlert)

    def markOperationAsVisited(self, operationID):
        self.update(operationsVisited=self.operationsVisited | {operationID})


class _DQSettings(utils.SettingRecord):

    def __init__(self, lastVisitedDQTabIdx=None, premMissionsTabDiscovered=False, *args, **kwargs):
        super(_DQSettings, self).__init__(lastVisitedDQTabIdx=lastVisitedDQTabIdx, premMissionsTabDiscovered=premMissionsTabDiscovered)

    def setLastVisitedDQTab(self, lastVisitedDQTabIdx):
        self.update(lastVisitedDQTabIdx=lastVisitedDQTabIdx)

    def onPremMissionsTabDiscovered(self):
        self.update(premMissionsTabDiscovered=True)


class _DogTagsRootSettings(utils.SettingRootRecord):

    def __init__(self, lastVisitedDogTagsTabIdx=None, onboardingEnabled=True, seenComps=None):
        super(_DogTagsRootSettings, self).__init__(lastVisitedDogTagsTabIdx=lastVisitedDogTagsTabIdx, onboardingEnabled=onboardingEnabled, seenComps=seenComps or set())

    def setLastVisitedDogTagsTab(self, lastVisitedDogTagsTabIdx):
        self.update(lastVisitedDogTagsTabIdx=lastVisitedDogTagsTabIdx)

    def setOnboardingEnabled(self, onboardingEnabled):
        self.update(onboardingEnabled=onboardingEnabled)

    def markComponentAsSeen(self, compId):
        self.update(seenComps=self.seenComps | {compId})

    @classmethod
    def _getSettingName(cls):
        return DOG_TAGS


class _WotPlusSettings(utils.SettingRootRecord):

    def __init__(self, isFirstTime=True, isWotPlusEnabled=False, isEntryPointsEnabled=False, isGoldReserveEnabled=False, isPassiveXpEnabled=False, isTankRentalEnabled=False, isFreeDirectivesEnabled=False, isFreeDemountingEnabled=False, isExcludedMapEnabled=False, rentPendingVehCD=None, isExclusiveVehicleEnabled=False):
        super(_WotPlusSettings, self).__init__(isFirstTime=isFirstTime, isWotPlusEnabled=isWotPlusEnabled, isEntryPointsEnabled=isEntryPointsEnabled, isGoldReserveEnabled=isGoldReserveEnabled, isPassiveXpEnabled=isPassiveXpEnabled, isTankRentalEnabled=isTankRentalEnabled, isFreeDirectivesEnabled=isFreeDirectivesEnabled, isFreeDemountingEnabled=isFreeDemountingEnabled, isExcludedMapEnabled=isExcludedMapEnabled, isExclusiveVehicleEnabled=isExclusiveVehicleEnabled, rentPendingVehCD=rentPendingVehCD)

    def setIsFirstTime(self, isFirstTime):
        self.update(isFirstTime=isFirstTime)

    def setWotPlusEnabledState(self, isEnabled):
        self.update(isWotPlusEnabled=isEnabled)

    def setEntryPointsEnabledState(self, isEnabled):
        self.update(isEntryPointsEnabled=isEnabled)

    def setGoldReserveEnabledState(self, isEnabled):
        self.update(isGoldReserveEnabled=isEnabled)

    def setPassiveXpState(self, isEnabled):
        self.update(isPassiveXpEnabled=isEnabled)

    def setTankRentalState(self, isEnabled):
        self.update(isTankRentalEnabled=isEnabled)

    def setFreeDirectivesState(self, isEnabled):
        self.update(isFreeDirectivesEnabled=isEnabled)

    def setFreeDemountingState(self, isEnabled):
        self.update(isFreeDemountingEnabled=isEnabled)

    def setExcludedMapState(self, isEnabled):
        self.update(isExcludedMapEnabled=isEnabled)

    def setRentPending(self, vehCD):
        self.update(rentPendingVehCD=vehCD)

    @classmethod
    def _getSettingName(cls):
        return WOT_PLUS


class _TelecomRentalsSettings(utils.SettingRootRecord):

    def __init__(self, isTelecomRentalsEnabled=False, isTelecomRentalsBlocked=False, pendingRentals=None):
        super(_TelecomRentalsSettings, self).__init__(isTelecomRentalsEnabled=isTelecomRentalsEnabled, isTelecomRentalsBlocked=isTelecomRentalsBlocked, pendingRentals=pendingRentals or set())

    def setTelecomRentalsEnabledState(self, isEnabled):
        self.update(isTelecomRentalsEnabled=isEnabled)

    def setTelecomRentalsBlockedState(self, isBlocked):
        self.update(isTelecomRentalsBlocked=isBlocked)

    def setRentPending(self, vehCD):
        self.update(pendingRentals=self.pendingRentals | {vehCD})

    def resetRentPending(self, vehCD):
        self.pendingRentals.discard(vehCD)
        self.update(pendingRentals=self.pendingRentals)

    @classmethod
    def _getSettingName(cls):
        return TELECOM_RENTALS


class _QuestSettings(utils.SettingRootRecord):

    def __init__(self, lastVisitTime=-1, visited=None, naVisited=None, minimized=None, personalMissions=None, dailyQuests=None, questDeltas=None):
        super(_QuestSettings, self).__init__(lastVisitTime=lastVisitTime, visited=visited or set(), naVisited=naVisited or set(), minimized=minimized or set(), personalMissions=_PMSettings(**(personalMissions or {})), dailyQuests=_DQSettings(**(dailyQuests or {})), questDeltas=questDeltas or dict())

    def updateVisited(self, visitSettingName, eventID):
        settingsValue = set(self[visitSettingName])
        if eventID not in settingsValue:
            self.update(**{visitSettingName: tuple(settingsValue | {eventID})})
            return True
        return False

    def removeCompleted(self, completedIDs):
        self.update(visited=tuple(set(self.visited).difference(completedIDs)))
        self.update(naVisited=tuple(set(self.naVisited).difference(completedIDs)))

    def updateExpanded(self, eventID, isExpanded):
        settingsValue = set(self['minimized'])
        if isExpanded:
            self.update(minimized=tuple(settingsValue.difference([eventID])))
        else:
            self.update(minimized=tuple(settingsValue.union([eventID])))

    def save(self):
        self.update(lastVisitTime=time.time())
        super(_QuestSettings, self).save()

    def _asdict(self):
        result = super(_QuestSettings, self)._asdict()
        result.update(personalMissions=self.personalMissions._asdict())
        result.update(dailyQuests=self.dailyQuests._asdict())
        return result

    @classmethod
    def _getSettingName(cls):
        return 'quests'


def get():
    return _QuestSettings.load()


def isNewCommonEvent(svrEvent, settings=None):
    settings = settings or get()
    if svrEvent.isAvailable()[0]:
        setting = 'visited'
    else:
        setting = 'naVisited'
    return settings is not None and svrEvent.getID() not in settings[setting] and not svrEvent.isCompleted() and not svrEvent.isOutOfDate()


def isGroupMinimized(groupID, settings=None):
    settings = settings or get()
    return groupID in settings['minimized']


def getNewCommonEvents(events):
    settings = get()
    return [ e for e in events if isNewCommonEvent(e, settings) ]


@dependency.replace_none_kwargs(eventsCache=IEventsCache)
def visitEventGUI(event, counters=(), eventsCache=None):
    if event is None:
        return
    else:
        s = get()
        isNaVisitedChanged = s.updateVisited('naVisited', event.getID())
        if event.isAvailable()[0]:
            isVisitedChanged = s.updateVisited('visited', event.getID())
        else:
            isVisitedChanged = False
        if isNaVisitedChanged or isVisitedChanged:
            s.save()
            converted = {}
            for counter in counters:
                key, value = counter(eventsCache)
                converted[key] = value

            eventsCache.onEventsVisited(converted)
        return


def visitEventsGUI(events):
    if events:
        for event in events:
            visitEventGUI(event)


def expandGroup(groupID, isExpanded):
    if groupID is None:
        return
    else:
        s = get()
        s.updateExpanded(groupID, isExpanded)
        s.save()
        return


def updateCommonEventsSettings(svrEvents):
    s = get()
    s.removeCompleted(set(e.getID() for e in svrEvents.itervalues() if e.isCompleted()))
    s.save()


def _updatePMSettings(**kwargs):
    settings = get()
    settings.personalMissions.update(**kwargs)
    settings.save()


def isPMOperationNew(operationID, pmSettings=None):
    pqSettings = pmSettings or get()
    return operationID not in pqSettings.personalMissions.operationsVisited


def isNeedToShowHeaderAlert():
    return get().personalMissions.headerAlert


def markHeaderAlertAsVisited():
    _updatePMSettings(headerAlert=True)


def getDQSettings():
    return get().dailyQuests


@contextmanager
def dailyQuestSettings():
    s = get()
    yield s.dailyQuests
    s.save()


def getDogTagsSettings():
    return _DogTagsRootSettings.load()


@contextmanager
def dogTagsSettings():
    s = getDogTagsSettings()
    yield s
    s.save()


def getWotPlusSettings():
    return _WotPlusSettings.load()


@contextmanager
def wotPlusSettings():
    s = getWotPlusSettings()
    yield s
    s.save()


def getTelecomRentalsSettings():
    return _TelecomRentalsSettings.load()


@contextmanager
def telecomRentalsSettings():
    s = getTelecomRentalsSettings()
    yield s
    s.save()