# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/trade_in_builders.py
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips.builders import DataBuilder, DefaultFormatBuilder
from gui.shared.tooltips import trade_in
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.TRADE_IN_INFO, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, trade_in.TradeInInfoTooltipData(contexts.ToolTipContext(None))),
     DefaultFormatBuilder(TOOLTIPS_CONSTANTS.TRADE_IN_INFO_NOT_AVAILABLE, TOOLTIPS_CONSTANTS.COMPLEX_UI, trade_in.TradeInInfoNotAvailableData(contexts.ToolTipContext(None))),
     DefaultFormatBuilder(TOOLTIPS_CONSTANTS.TRADE_IN_STATE_NOT_AVAILABLE, TOOLTIPS_CONSTANTS.COMPLEX_UI, trade_in.TradeInStateNotAvailableData(contexts.ToolTipContext(None))))