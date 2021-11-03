# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/avatar_components/avatar_respawn_mechanic.py
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS
from helpers.EffectsList import RespawnDestroyEffect
from debug_utils import LOG_DEBUG_DEV

class AvatarRespawnMechanic(object):
    respawnEnabled = property(lambda self: self.__enabled)

    def __init__(self):
        self.__enabled = False

    def onBecomePlayer(self):
        self.__enabled = BONUS_CAPS.checkAny(self.arenaBonusType, BONUS_CAPS.RESPAWN)
        if not self.__enabled:
            return

    def handleKey(self, isDown, key, mods):
        return False

    def onBecomeNonPlayer(self):
        if not self.__enabled:
            return

    def updateRespawnVehicles(self, vehsList):
        if not self.__enabled:
            return
        else:
            ctrl = self.guiSessionProvider.dynamic.respawn
            if ctrl is not None:
                ctrl.updateRespawnVehicles(vehsList)
            return

    def updateRespawnCooldowns(self, cooldowns):
        if not self.__enabled:
            return
        else:
            LOG_DEBUG_DEV('updateRespawnCooldowns ', cooldowns)
            cooldowns = {item['vehTypeCompDescr']:item['endOfCooldownPiT'] for item in cooldowns}
            ctrl = self.guiSessionProvider.dynamic.respawn
            if ctrl is not None:
                ctrl.updateRespawnCooldowns(cooldowns)
            return

    def updateRespawnInfo(self, respawnInfo):
        if not self.__enabled:
            return
        else:
            ctrl = self.guiSessionProvider.dynamic.respawn
            if ctrl is not None:
                ctrl.updateRespawnInfo(respawnInfo)
            return

    def updateVehicleLimits(self, respawnLimits):
        if not self.__enabled:
            return
        else:
            respawnLimits = {item['group']:item['vehTypeCompDescrs'] for item in respawnLimits}
            ctrl = self.guiSessionProvider.dynamic.respawn
            if ctrl is not None:
                ctrl.updateVehicleLimits(respawnLimits)
            return

    def explodeVehicleBeforeRespawn(self, vehID):
        if BONUS_CAPS.checkAny(self.arenaBonusType, BONUS_CAPS.HALLOWEEN):
            return
        RespawnDestroyEffect.play(vehID)

    def updatePlayerLives(self, lives):
        LOG_DEBUG_DEV('updatePlayerLives', lives)
        ctrl = self.guiSessionProvider.dynamic.respawn
        if ctrl is not None:
            ctrl.updatePlayerRespawnLives(lives)
        return

    def onTeamLivesRestored(self, teams):
        LOG_DEBUG_DEV('onTeamLivesRestored', teams)
        ctrl = self.guiSessionProvider.dynamic.respawn
        if ctrl is not None:
            ctrl.restoredTeamRespawnLives(teams)
        return