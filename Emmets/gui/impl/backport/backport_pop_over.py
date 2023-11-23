# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/backport/backport_pop_over.py
from collections import namedtuple
import logging
from frameworks.wulf import ViewSettings, ViewModel
from gui.impl.gen import R
from gui.impl.pub import PopOverViewImpl
from gui.shared import g_eventBus
from gui.shared.events import HidePopoverEvent
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
_logger = logging.getLogger(__name__)
_PopOverData = namedtuple('PopOverData', ('alias', 'args'))

def createPopOverData(alias, args=None):
    return _PopOverData(alias, args)


class BackportPopOverContent(PopOverViewImpl):
    __appLoader = dependency.descriptor(IAppLoader)
    __slots__ = ()

    def __init__(self, popOverData):
        settings = ViewSettings(R.views.common.pop_over_window.backport_pop_over.BackportPopOverContent())
        settings.model = ViewModel()
        settings.kwargs = {'alias': popOverData.alias, 'data': popOverData.args}
        super(BackportPopOverContent, self).__init__(settings)

    def _initialize(self, alias, data):
        super(BackportPopOverContent, self)._initialize()
        popoverManager = self.__appLoader.getApp().popoverManager
        if popoverManager is None:
            _logger.error("popoverManager doesn't exist.")
            return
        else:
            popoverManager.requestShowPopover(alias, data)
            g_eventBus.addListener(HidePopoverEvent.POPOVER_DESTROYED, self.__onPopOverDestroy)
            return

    def _finalize(self):
        g_eventBus.removeListener(HidePopoverEvent.POPOVER_DESTROYED, self.__onPopOverDestroy)
        popoverManager = self.__appLoader.getApp().popoverManager
        if popoverManager is not None:
            popoverManager.requestHidePopover()
        super(BackportPopOverContent, self)._finalize()
        return

    def __onPopOverDestroy(self, _):
        self.destroyWindow()