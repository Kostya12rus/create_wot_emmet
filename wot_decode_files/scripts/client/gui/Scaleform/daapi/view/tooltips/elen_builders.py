# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/elen_builders.py
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips import elen
from gui.shared.tooltips.builders import DataBuilder
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.EVENT_QUESTS_PREVIEW, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, elen.ElenPreviewTooltipData(contexts.QuestsBoosterContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.EVENT_BOARDS_BADGE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, elen.BadgeTooltipData(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.EVENT_BOARDS_BADGES_GROUP, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, elen.BabgesGroupTooltipData(contexts.QuestContext())))