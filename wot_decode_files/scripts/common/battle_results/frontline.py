# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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
  'flXPReplay', str, '', ValueReplayPacker(), 'skip', ENTRY_TYPE.ACCOUNT_ALL)]