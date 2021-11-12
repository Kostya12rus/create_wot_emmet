# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/tooltips/shop_sales/paid_shuffle_tooltip.py
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from gui.shared.tooltips import formatters
from gui.shared.tooltips.common import BlocksTooltipData
BLOCK_WIDTH = 700

class PaidShuffleTooltip(BlocksTooltipData):

    def __init__(self, context):
        super(PaidShuffleTooltip, self).__init__(context, None)
        self._setContentMargin(bottom=10, top=2)
        return

    def _packBlocks(self, *args, **kwargs):
        return [
         formatters.packImageTextBlockData(title=text_styles.main(backport.text(R.strings.tooltips.shopSales.paidShuffle.header(), start_time=text_styles.neutral(backport.text(R.strings.tooltips.shopSales.paidShuffle.startTime())))), img=backport.image(R.images.gui.maps.icons.shopSales.clock()), txtPadding=formatters.packPadding(top=15, left=-10), imgPadding=formatters.packPadding(top=7, left=-12, right=5), blockWidth=BLOCK_WIDTH)]