# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_results/settings.py


class BATTLE_RESULTS_RECORD(object):
    ARENA_UNIQUE_ID = 'arenaUniqueID'
    COMMON = 'common'
    PERSONAL = 'personal'
    PLAYERS = 'players'
    VEHICLES = 'vehicles'
    AVATARS = 'avatars'
    TOP_LEVEL_RECORDS = (
     COMMON, PERSONAL, PLAYERS, VEHICLES, AVATARS)
    PERSONAL_AVATAR = 'avatar'
    COMMON_BOTS = 'bots'


class PREMIUM_STATE(object):
    NONE = 0
    HAS_ALREADY = 1
    BUY_ENABLED = 2
    BOUGHT = 4


class PROGRESS_ACTION(object):
    RESEARCH_UNLOCK_TYPE = 'UNLOCK_LINK_TYPE'
    PURCHASE_UNLOCK_TYPE = 'PURCHASE_LINK_TYPE'
    NEW_SKILL_UNLOCK_TYPE = 'NEW_SKILL_LINK_TYPE'
    NEW_FREE_SKILL_UNLOCK_TYPE = 'NEW_FREE_SKILL_LINK_TYPE'


class PLAYER_TEAM_RESULT(object):
    WIN = 'win'
    DEFEAT = 'lose'
    DRAW = 'tie'
    ENDED = 'ended'


class FACTOR_VALUE(object):
    BASE_CREDITS_FACTOR = 100
    PREMUIM_CREDITS_FACTOR = 150
    PREMUIM_PLUS_CREDITS_FACTOR = 150
    BASE_XP_FACTOR = 100
    PREMUIM_XP_FACTOR = 150
    PREMUIM_PLUS_XP_FACTOR = 150
    ADDITIONAL_BONUS_ZERO_FACTOR = 0
    ADDITIONAL_BONUS_ONE_FACTOR = 10


class EMBLEM_TYPE(object):
    CLAN = 1


class UI_VISIBILITY(object):
    SHOW_SQUAD = 1
    SHOW_RESOURCES = 2