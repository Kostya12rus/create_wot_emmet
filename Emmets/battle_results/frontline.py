# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/battle_results/frontline.py
from battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
from DictPackers import ValueReplayPacker
BATTLE_RESULTS = [
 (
  'creditsAfterShellCosts', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'unchargedShellCosts', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'prevMetaLevel', tuple, (1, 0), None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'metaLevel', tuple, (1, 0), None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'flXP', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'originalFlXP', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'subtotalFlXP', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'boosterFlXP', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'boosterFlXPFactor100', int, 0, None, 'any', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'flXPReplay', str, '', ValueReplayPacker(), 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'bpChapter', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'basePointsDiff', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'bpNonChapterPointsDiff', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'sumPoints', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'hasBattlePass', bool, False, None, 'skip', ENTRY_TYPE.ACCOUNT_ALL)]