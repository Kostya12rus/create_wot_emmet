# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/battle_results/event.py
from battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
from DictPackers import ValueReplayPacker
BATTLE_RESULTS = [
 (
  'eventPoints', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  'eventPointsLeft', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  'eventPointsTotal', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  'environmentID', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  'difficultyLevel', int, 0, None, 'any', ENTRY_TYPE.VEHICLE_ALL),
 (
  'eventAFKViolator', bool, False, None, 'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  'eventAFKBanned', bool, False, None, 'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  'hwRewardBoxKeys', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  'hwRewardBoxBossKeys', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  'hwTeamFightPlace', int, -1, None, 'any', ENTRY_TYPE.VEHICLE_ALL),
 (
  'hwBossFightPlace', int, -1, None, 'any', ENTRY_TYPE.VEHICLE_ALL)]