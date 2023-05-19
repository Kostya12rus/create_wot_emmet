# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/comp7_common.py
import enum
ROLE_EQUIPMENT_TAG = 'roleEquipment'
COMP7_QUEST_PREFIX = 'comp7_2023_1'
COMP7_QUEST_DELIMITER = '_'
COMP7_TOKEN_WEEKLY_REWARD_NAME = 'comp7_2023_1_weekly_rewards_token'

@enum.unique
class Comp7QuestType(enum.Enum):
    RANKS = 'ranks'
    TOKENS = 'token'
    PERIODIC = 'period'
    ACTIVITY = 'activity'
    WEEKLY = 'weekly'


CLIENT_VISIBLE_QUESTS_TYPE = (
 Comp7QuestType.TOKENS,
 Comp7QuestType.RANKS,
 Comp7QuestType.PERIODIC,
 Comp7QuestType.WEEKLY)