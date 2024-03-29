# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/bootcamp_builders.py
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips import bootcamp
from gui.shared.tooltips.builders import DataBuilder
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.BOOTCAMP_AWARD_MEDAL, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, bootcamp.StatsTooltipData(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.BOOTCAMP_REWARD_PROGRESS, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, bootcamp.ProgressRewardTooltipData(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.BOOTCAMP_LESSON_PROGRESS, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, bootcamp.ProgressLessonTooltipData(contexts.ToolTipContext(None))))