# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/avatar_components/team_healthbar_mechanic.py
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS

class TeamHealthbarMechanic(object):

    def __init__(self):
        self.__enabled = False
        self.__lastTeamHealthPercentage = None
        return

    def handleKey(self, isDown, key, mods):
        return False

    def onBecomePlayer(self):
        self.__enabled = BONUS_CAPS.checkAny(self.arenaBonusType, BONUS_CAPS.TEAM_HEALTH_BAR)
        if not self.__enabled:
            return
        else:
            self.__lastTeamHealthPercentage = None
            return

    def onBecomeNonPlayer(self):
        if not self.__enabled:
            return
        else:
            self.__lastTeamHealthPercentage = None
            return

    def updateTeamsHealthPercentage(self, teamsHealthPercentage):
        if not self.__enabled:
            return
        self.__lastTeamHealthPercentage = teamsHealthPercentage
        self.arena.updateTeamHealthPercent(teamsHealthPercentage)

    def getHealthPercentage(self):
        return self.__lastTeamHealthPercentage