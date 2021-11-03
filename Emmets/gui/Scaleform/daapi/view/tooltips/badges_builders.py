# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/badges_builders.py
from gui.Scaleform.daapi.view.lobby.badges_tooltips import BadgesSuffixItem, BadgesSuffixRankedItem
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips.builders import DataBuilder
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.BADGES_SUFFIX_ITEM, TOOLTIPS_CONSTANTS.BADGES_SUFFIX_ITEM_UI, BadgesSuffixItem(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.BADGES_SUFFIX_RANKED_ITEM, TOOLTIPS_CONSTANTS.BADGES_SUFFIX_RANKED_ITEM_UI, BadgesSuffixRankedItem(contexts.ToolTipContext(None))))