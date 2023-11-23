# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleResultsMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class BattleResultsMeta(AbstractWindowView):

    def saveSorting(self, iconType, sortDirection, bonusType):
        self._printOverrideError('saveSorting')

    def showEventsWindow(self, questID, eventType):
        self._printOverrideError('showEventsWindow')

    def getClanEmblem(self, uid, clanID):
        self._printOverrideError('getClanEmblem')

    def onResultsSharingBtnPress(self):
        self._printOverrideError('onResultsSharingBtnPress')

    def showUnlockWindow(self, itemId, unlockType):
        self._printOverrideError('showUnlockWindow')

    def showProgressiveRewardView(self):
        self._printOverrideError('showProgressiveRewardView')

    def onAppliedPremiumBonus(self):
        self._printOverrideError('onAppliedPremiumBonus')

    def onShowDetailsPremium(self):
        self._printOverrideError('onShowDetailsPremium')

    def showDogTagWindow(self, componentId):
        self._printOverrideError('showDogTagWindow')

    def showVehicleStats(self, vehCD):
        self._printOverrideError('showVehicleStats')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setClanEmblemS(self, uid, iconTag):
        if self._isDAAPIInited():
            return self.flashObject.as_setClanEmblem(uid, iconTag)

    def as_setTeamInfoS(self, uid, iconTag, teamName):
        if self._isDAAPIInited():
            return self.flashObject.as_setTeamInfo(uid, iconTag, teamName)

    def as_setIsInBattleQueueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsInBattleQueue(value)