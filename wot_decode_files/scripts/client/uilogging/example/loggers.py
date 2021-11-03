# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/example/loggers.py
import typing
from uilogging.base.logger import BaseLogger, ifUILoggingEnabled
from uilogging.base.mixins import LogOnceMixin, TimedActionMixin
from wotdecorators import noexcept
if typing.TYPE_CHECKING:
    from uilogging.example.views import BuyProductView

class ExampleLogger(TimedActionMixin, LogOnceMixin, BaseLogger):

    def __init__(self, group):
        super(ExampleLogger, self).__init__('example', group)

    @noexcept
    @ifUILoggingEnabled()
    def highlightProduct(self, view, product):
        highlighted = [ p.name for p in view.products.values() if p.highlighted ]
        self.info('highlight', product=product, highlighted=highlighted)


class ExampleTooltipLogger(ExampleLogger):

    def __init__(self):
        super(ExampleTooltipLogger, self).__init__('tooltip_view')
        self._openedTooltip = None
        return

    @noexcept
    @ifUILoggingEnabled()
    def tooltipOpened(self, tooltip):
        self._openedTooltip = tooltip
        self.startAction('tooltip_opened')

    @noexcept
    @ifUILoggingEnabled()
    def tooltipClosed(self, tooltip, timeLimit):
        if self._openedTooltip and self._openedTooltip == tooltip:
            self._openedTooltip = None
            self.stopAction('tooltip_opened', tooltip=tooltip, timeLimit=timeLimit)
        return