# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/limited_ui/loggers.py
import typing
from uilogging.base.logger import MetricsLogger
from uilogging.limited_ui.constants import FEATURE, LimitedUILogActions
if typing.TYPE_CHECKING:
    from uilogging.types import ItemType, ParentScreenType

class LimitedUILogger(MetricsLogger):
    __slots__ = ()

    def __init__(self):
        super(LimitedUILogger, self).__init__(FEATURE)

    def handleClickOnce(self, item, parentScreen):
        self.logOnce(action=LimitedUILogActions.CLICK, item=item, parentScreen=parentScreen)