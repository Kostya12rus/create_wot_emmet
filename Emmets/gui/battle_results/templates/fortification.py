# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_results/templates/fortification.py
from gui.battle_results.components import common
from gui.battle_results.templates import regular
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
regular.FINISH_RESULT_VO_META.bind(common.StrongholdBattleFinishResultBlock)
STRONGHOLD_BATTLE_COMMON_STATS_BLOCK = regular.REGULAR_COMMON_STATS_BLOCK.clone()
STRONGHOLD_BATTLE_COMMON_STATS_BLOCK.addNextComponent(common.StrongholdBattleFinishResultBlock(None, '', _RECORD.PERSONAL, _RECORD.PERSONAL_AVATAR))