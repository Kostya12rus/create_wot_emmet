# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/missions/missions_helpers.py
import typing
from helpers import dependency
from skeletons.gui.server_events import IEventsCache
if typing.TYPE_CHECKING:
    from typing import Iterable
    from gui.impl.gen.view_models.common.missions.event_model import EventModel
    from gui.server_events.event_items import Quest, DailyQuest
    from frameworks.wulf.view.array import Array
__all__ = ('needToUpdateQuestsInModel', )
NUM_OF_COMMON_DAILY_QUESTS = 3

def areCommonQuestsCompleted(quests):
    numCompletedQuests = len([ q for q in quests if q.isCompleted() ])
    return numCompletedQuests >= NUM_OF_COMMON_DAILY_QUESTS


def needToUpdateQuestsInModel(quests, questsInModel):
    questIds = [ q.getID() for q in quests ]
    return __hasProgressChanged(questIds) or __hasStatusChanged(questIds) or __hasDifferentQuests(questIds, __questModelsIdGen(questsInModel))


@dependency.replace_none_kwargs(eventsCache=IEventsCache)
def __hasProgressChanged(ids, eventsCache=None):
    hasProgressedFunc = eventsCache.questsProgress.hasQuestProgressed
    return any(hasProgressedFunc(index) for index in ids)


@dependency.replace_none_kwargs(eventsCache=IEventsCache)
def __hasStatusChanged(ids, eventsCache=None):
    for index in ids:
        if eventsCache.questsProgress.getQuestCompletionChanged(index):
            return True

    return False


def __hasDifferentQuests(questIds, viewModelIds):
    return sorted(questIds) != sorted(viewModelIds)


def __questModelsIdGen(dailyQuests):
    for dailyQuest in dailyQuests:
        yield dailyQuest.getId()