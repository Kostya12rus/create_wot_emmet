# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleSessionWindowMeta.py
from gui.Scaleform.daapi.view.lobby.prb_windows.PrebattleWindow import PrebattleWindow

class BattleSessionWindowMeta(PrebattleWindow):

    def requestToAssignMember(self, accId):
        self._printOverrideError('requestToAssignMember')

    def requestToUnassignMember(self, accId):
        self._printOverrideError('requestToUnassignMember')

    def canMoveToAssigned(self, accId):
        self._printOverrideError('canMoveToAssigned')

    def canMoveToUnassigned(self, accId):
        self._printOverrideError('canMoveToUnassigned')

    def setSelectedFilter(self, value):
        self._printOverrideError('setSelectedFilter')

    def onCantMoveS(self, accId):
        self._printOverrideError('onCantMoveS')

    def as_setStartTimeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setStartTime(value)

    def as_setTotalPlayersCountS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTotalPlayersCount(value)

    def as_setInfoS(self, isTurnamentBattle, wins, map, firstTeam, secondTeam, count, description, comment, unitLetter, vehicleLevel, teamIndex):
        if self._isDAAPIInited():
            return self.flashObject.as_setInfo(isTurnamentBattle, wins, map, firstTeam, secondTeam, count, description, comment, unitLetter, vehicleLevel, teamIndex)

    def as_setWinnerIfDrawS(self, value=0):
        if self._isDAAPIInited():
            return self.flashObject.as_setWinnerIfDraw(value)

    def as_setNationsLimitsS(self, nations):
        if self._isDAAPIInited():
            return self.flashObject.as_setNationsLimits(nations)

    def as_setClassesLimitsS(self, vehicleLevels, classesLimitsAreIdentical):
        if self._isDAAPIInited():
            return self.flashObject.as_setClassesLimits(vehicleLevels, classesLimitsAreIdentical)

    def as_setCommonLimitsS(self, teamLevel, maxPlayers):
        if self._isDAAPIInited():
            return self.flashObject.as_setCommonLimits(teamLevel, maxPlayers)

    def as_setPlayersCountTextS(self, playersCountText):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayersCountText(playersCountText)

    def as_setFiltersS(self, data, selectedIndex):
        if self._isDAAPIInited():
            return self.flashObject.as_setFilters(data, selectedIndex)