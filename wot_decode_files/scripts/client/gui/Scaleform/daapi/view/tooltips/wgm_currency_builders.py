# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/wgm_currency_builders.py
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips import wgm_currency
from gui.shared.tooltips.builders import DataBuilder
__all__ = ('getTooltipBuilders', )

class CurrencyTooltipBuilder(DataBuilder):
    __slots__ = ('__btnType', '__hideActionBlock')

    def __init__(self, btnType, tooltipType, linkage, hideActionBlock=False):
        super(CurrencyTooltipBuilder, self).__init__(tooltipType, linkage, wgm_currency.WGMCurrencyTooltip(contexts.ToolTipContext(None)))
        self.__btnType = btnType
        self.__hideActionBlock = hideActionBlock
        return

    def _buildData(self, advanced, *args):
        return super(CurrencyTooltipBuilder, self)._buildData(advanced, self.__btnType, self.__hideActionBlock)


def getTooltipBuilders():
    return (
     CurrencyTooltipBuilder(CURRENCIES_CONSTANTS.GOLD, TOOLTIPS_CONSTANTS.GOLD_STATS, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI),
     CurrencyTooltipBuilder(CURRENCIES_CONSTANTS.CREDITS, TOOLTIPS_CONSTANTS.CREDITS_STATS, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI),
     CurrencyTooltipBuilder(CURRENCIES_CONSTANTS.CREDITS, TOOLTIPS_CONSTANTS.CREDITS_STATS_FULL_SCREEN, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, True),
     CurrencyTooltipBuilder(CURRENCIES_CONSTANTS.GOLD, TOOLTIPS_CONSTANTS.GOLD_STATS_FULL_SCREEN, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, True))