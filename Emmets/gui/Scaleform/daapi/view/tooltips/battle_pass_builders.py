# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/battle_pass_builders.py
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts, battle_pass
from gui.shared.tooltips.builders import DataBuilder
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.BATTLE_PASS_GIFT_TOKEN, TOOLTIPS_CONSTANTS.BATTLE_PASS_GIFT_TOKEN_UI, battle_pass.BattlePassGiftTokenTooltipData(contexts.BattlePassGiftTokenContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.BATTLE_PASS_POINTS, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, battle_pass.BattlePassPointsTooltipData(contexts.ToolTipContext(None))))