# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/account_completion_builders.py
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.impl.backport.backport_tooltip import DecoratedTooltipWindow
from gui.impl.lobby.account_completion.tooltips.hangar_tooltip_view import HangarTooltipView
from gui.shared.tooltips import ToolTipBaseData
from gui.shared.tooltips import contexts
from gui.shared.tooltips.builders import TooltipWindowBuilder
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     TooltipWindowBuilder(TOOLTIPS_CONSTANTS.ACCOUNT_COMPLETION, None, AccountCompletionTooltipData(contexts.ToolTipContext(None))),)


class AccountCompletionTooltipData(ToolTipBaseData):

    def __init__(self, context):
        super(AccountCompletionTooltipData, self).__init__(context, TOOLTIPS_CONSTANTS.ACCOUNT_COMPLETION)

    def getDisplayableData(self, email=None):
        return DecoratedTooltipWindow(HangarTooltipView(email), useDecorator=False)