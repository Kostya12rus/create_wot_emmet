# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/HangarHeaderMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class HangarHeaderMeta(BaseDAAPIComponent):

    def onQuestBtnClick(self, questType, questID):
        self._printOverrideError('onQuestBtnClick')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_createBattlePassS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_createBattlePass()

    def as_removeBattlePassS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_removeBattlePass()

    def as_createRankedBattlesS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_createRankedBattles()

    def as_removeRankedBattlesS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_removeRankedBattles()

    def as_createBattleRoyaleS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_createBattleRoyale()

    def as_removeBattleRoyaleS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_removeBattleRoyale()

    def as_createBattleRoyaleTournamentS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_createBattleRoyaleTournament()

    def as_removeBattleRoyaleTournamentS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_removeBattleRoyaleTournament()

    def as_createEpicWidgetS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_createEpicWidget()

    def as_removeEpicWidgetS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_removeEpicWidget()

    def as_createFunRandomWidgetS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_createFunRandomWidget()

    def as_removeFunRandomWidgetS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_removeFunRandomWidget()

    def as_setSecondaryEntryPointVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSecondaryEntryPointVisible(value)

    def as_setResourceWellEntryPointS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setResourceWellEntryPoint(value)

    def as_setBattleMattersEntryPointS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setBattleMattersEntryPoint(value)

    def as_setCollectiveGoalEntryPointS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCollectiveGoalEntryPoint(value)

    def as_setArmoryYardEntryPointS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setArmoryYardEntryPoint(value)

    def as_createComp7S(self):
        if self._isDAAPIInited():
            return self.flashObject.as_createComp7()

    def as_removeComp7S(self):
        if self._isDAAPIInited():
            return self.flashObject.as_removeComp7()