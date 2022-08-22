# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/epicBattle/epic_quest_progress_view.py
from gui.Scaleform.daapi.view.meta.EpicQuestProgressInfoMeta import EpicQuestProgressInfoMeta
from gui.shared import g_eventBus, events
from helpers import dependency
from skeletons.gui.battle_results import IBattleResultsService

class EpicQuestProgressView(EpicQuestProgressInfoMeta):
    __slots__ = ()
    __battleResults = dependency.descriptor(IBattleResultsService)

    def showQuestById(self, questId, eventType):
        g_eventBus.handleEvent(events.LobbySimpleEvent(events.LobbySimpleEvent.BATTLE_RESULTS_SHOW_QUEST, ctx={'questId': questId, 
           'eventType': eventType}))

    def updateQuestsInfo(self, arenaUniqueID):
        battleResultsVO = self.__battleResults.getResultsVO(arenaUniqueID)
        if not battleResultsVO:
            return
        quests = []
        quests.extend(battleResultsVO.get('battlePass', []))
        quests.extend(battleResultsVO.get('quests', []))
        questsArray = []
        for quest in quests:
            questInfo = quest['questInfo']
            questModel = {'id': questInfo['questID'], 
               'eventType': questInfo['eventType'], 
               'name': quest.get('title', '') or questInfo.get('description', ''), 
               'progressList': quest['progressList'], 
               'status': questInfo['status'], 
               'statusTooltip': questInfo.get('statusTooltip', '')}
            rewards = self.__getRewards(quest)
            if rewards:
                questModel['rewards'] = [
                 {'linkage': 'EpicQuestTextAwardBlockUI', 
                    'items': [
                            (', ').join(rewards)]}]
            questsArray.append(questModel)

        self.as_updateDataS(questsArray)

    @staticmethod
    def __getRewards(quest):
        awards = quest.get('awards', [])
        if not awards:
            return []
        return [ item for award in awards for item in award.get('items', []) ]