# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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