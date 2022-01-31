# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/new_year/__init__.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey
from gui.Scaleform.framework.managers.view_lifecycle_watcher import IViewLifecycleHandler

class DiscountPopoverHandler(IViewLifecycleHandler):

    def __init__(self, onViewCreatedCallback, onViewDestroyedCallback):
        super(DiscountPopoverHandler, self).__init__([
         ViewKey(VIEW_ALIAS.NY_SELECT_VEHICLE_FOR_DISCOUNT_POPOVER)])
        self.__onViewCreatedCallback = onViewCreatedCallback
        self.__onViewDestroyedCallback = onViewDestroyedCallback

    def onViewCreated(self, view):
        self.__onViewCreatedCallback()

    def onViewDestroyed(self, _):
        self.__onViewDestroyedCallback()