# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/tooltips/crew_book.py
from gui.shared.formatters import text_styles
from gui.shared.tooltips import TOOLTIP_TYPE, formatters
from gui.shared.tooltips.common import BlocksTooltipData

class CrewBookTooltipDataBlock(BlocksTooltipData):

    def __init__(self, context):
        super(CrewBookTooltipDataBlock, self).__init__(context, TOOLTIP_TYPE.CREW_BOOK)
        self._setContentMargin(bottom=8)
        self._setWidth(320)

    def _packBlocks(self, *args, **kwargs):
        items = super(CrewBookTooltipDataBlock, self)._packBlocks()
        item = self.context.buildItem(*args, **kwargs)
        block = []
        block.append(formatters.packTextBlockData(text=text_styles.highTitle(item.userName)))
        block.append(formatters.packTextBlockData(text=text_styles.main(item.fullDescription)))
        items.append(formatters.packBuildUpBlockData(block))
        return items