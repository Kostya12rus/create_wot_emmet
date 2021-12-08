# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/battle_results/battle_results_constants.py
from constants import ARENA_BONUS_TYPE
PATH_TO_CONFIG = {ARENA_BONUS_TYPE.REGULAR: 'random', 
   ARENA_BONUS_TYPE.EPIC_RANDOM: 'random', 
   ARENA_BONUS_TYPE.EPIC_RANDOM_TRAINING: 'random', 
   ARENA_BONUS_TYPE.RANKED: 'ranked', 
   ARENA_BONUS_TYPE.EPIC_BATTLE: 'frontline', 
   ARENA_BONUS_TYPE.EPIC_BATTLE_TRAINING: 'frontline', 
   ARENA_BONUS_TYPE.BATTLE_ROYALE_SOLO: 'battle_royale', 
   ARENA_BONUS_TYPE.BATTLE_ROYALE_SQUAD: 'battle_royale', 
   ARENA_BONUS_TYPE.BATTLE_ROYALE_TRN_SOLO: 'battle_royale', 
   ARENA_BONUS_TYPE.BATTLE_ROYALE_TRN_SQUAD: 'battle_royale', 
   ARENA_BONUS_TYPE.MAPBOX: 'random', 
   ARENA_BONUS_TYPE.MAPS_TRAINING: 'maps_training'}
POSSIBLE_TYPES = (
 int, float, str, bool, list, tuple, dict, set, None)

class BATTLE_RESULT_ENTRY_TYPE:
    COMMON = 1
    ACCOUNT_SELF = 2
    ACCOUNT_ALL = 3
    VEHICLE_SELF = 4
    VEHICLE_ALL = 5
    PLAYER_INFO = 6
    SERVER = 7
    ALL = (
     COMMON, ACCOUNT_SELF, ACCOUNT_ALL, VEHICLE_SELF, VEHICLE_ALL, PLAYER_INFO, SERVER)