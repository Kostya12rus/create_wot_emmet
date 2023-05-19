# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/cgf_script/bonus_caps_rules.py
import BigWorld, CGF
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS
from cgf_script.managers_registrator import autoregister
from constants import IS_CLIENT
if IS_CLIENT:
    from Avatar import PlayerAvatar
    from ClientArena import ClientArena

def bonusCapsManager(bonusCap, domain=CGF.DomainOption.DomainAll):

    def predicate(spaceID):
        player = BigWorld.player()
        if spaceID != ClientArena.DEFAULT_ARENA_WORLD_ID and isinstance(player, PlayerAvatar):
            return ARENA_BONUS_TYPE_CAPS.checkAny(player.arenaBonusType, bonusCap)
        return False

    return autoregister(creationPredicate=predicate, domain=domain)