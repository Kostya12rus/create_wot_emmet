# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/wot_plus_builders.py
from gui.shared.tooltips.builders import DataBuilder
from gui.shared.tooltips import common, contexts
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
__all__ = ('getTooltipBuilders', )

class WotPlusBuilder(DataBuilder):
    __slots__ = ()

    def __init__(self, tooltipType, linkage):
        super(WotPlusBuilder, self).__init__(tooltipType, linkage, common.WotPlusTooltipContentWindowData(contexts.ToolTipContext(None)))
        return

    def build(self, manager, formatType, advanced_, *args, **kwargs):
        return self._provider


def getTooltipBuilders():
    return (
     WotPlusBuilder(TOOLTIPS_CONSTANTS.WOT_PLUS, None),)