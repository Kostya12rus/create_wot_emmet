# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/battle_session/legacy/permissions.py
from gui.prb_control import prb_getters
from gui.prb_control.entities.base.legacy.permissions import LegacyPermissions
from gui.prb_control.entities.base.limits import TeamNoPlayersInBattle, MaxCount

class BattleSessionPermissions(LegacyPermissions):

    def canSendInvite(self):
        return super(BattleSessionPermissions, self).canSendInvite() and self._canAddPlayers()

    def canExitFromQueue(self):
        return self.isCreator(self._roles)

    @classmethod
    def isCreator(cls, roles):
        return False

    def canAssignToTeam(self, team=1, isSelfAssignment=False):
        result = super(BattleSessionPermissions, self).canAssignToTeam(team, isSelfAssignment)
        if not result:
            return False
        else:
            clientPrb = prb_getters.getClientPrebattle()
            result = False
            if clientPrb is not None:
                settings = prb_getters.getPrebattleSettings(prebattle=clientPrb)
                rosters = prb_getters.getPrebattleRosters(prebattle=clientPrb)
                prbType = prb_getters.getPrebattleType(clientPrb, settings)
                result, _ = TeamNoPlayersInBattle(prbType).check(rosters, team, settings.getTeamLimits(team))
            return result

    def _canAddPlayers(self):
        clientPrb = prb_getters.getClientPrebattle()
        result = False
        if clientPrb is not None:
            settings = prb_getters.getPrebattleSettings(prebattle=clientPrb)
            rosters = prb_getters.getPrebattleRosters(prebattle=clientPrb)
            result, _ = MaxCount().check(rosters, 1, settings.getTeamLimits(1))
        return result