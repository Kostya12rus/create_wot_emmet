# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/resource_well_builders.py
from gui.Scaleform.daapi.view.tooltips.common_builders import HeaderMoneyAndXpBuilder
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     HeaderMoneyAndXpBuilder(CURRENCIES_CONSTANTS.GOLD, TOOLTIPS_CONSTANTS.RESOURCE_WELL_GOLD, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, True),
     HeaderMoneyAndXpBuilder(CURRENCIES_CONSTANTS.CREDITS, TOOLTIPS_CONSTANTS.RESOURCE_WELL_CREDITS, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, True),
     HeaderMoneyAndXpBuilder(CURRENCIES_CONSTANTS.CRYSTAL, TOOLTIPS_CONSTANTS.RESOURCE_WELL_CRYSTAL, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, True),
     HeaderMoneyAndXpBuilder(CURRENCIES_CONSTANTS.FREE_XP, TOOLTIPS_CONSTANTS.RESOURCE_WELL_FREE_XP, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, True))