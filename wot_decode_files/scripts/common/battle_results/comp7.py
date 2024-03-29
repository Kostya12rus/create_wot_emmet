# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/battle_results/comp7.py
from battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
BATTLE_RESULTS = [
 (
  'comp7PrestigePoints', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  'roleSkillUsed', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  'healthRepair', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  'alliedHealthRepair', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  'comp7Rating', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  'comp7Rank', tuple, (0, 0), None, 'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  'comp7RatingDelta', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  'comp7TeamStats', dict, {}, None, 'skip', ENTRY_TYPE.SERVER),
 (
  'fareTeamPrestigePointsPosition', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_SELF)]