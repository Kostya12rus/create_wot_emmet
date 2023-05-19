# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/managers/PopoverManager.py
from debug_utils import LOG_ERROR
from gui.Scaleform.framework import g_entitiesFactories
from gui.Scaleform.framework.entities.abstract.PopoverManagerMeta import PopoverManagerMeta
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.shared.events import HidePopoverEvent

class PopoverManager(PopoverManagerMeta):

    def __init__(self, scope):
        super(PopoverManager, self).__init__()
        self.__scope = scope
        self.addListener(HidePopoverEvent.POPOVER_DESTROYED, self.__handlerDestroyPopover)

    def requestShowPopover(self, alias, data):
        event = g_entitiesFactories.makeShowPopoverEvent(SFViewLoadParams(alias), ctx={'data': data})
        if event is not None:
            self.fireEvent(event, scope=self.__scope)
        else:
            LOG_ERROR('Event of opening popover can not be created', alias)
        return

    def requestHidePopover(self):
        self.fireEvent(HidePopoverEvent(HidePopoverEvent.HIDE_POPOVER))

    def destroy(self):
        self.removeListener(HidePopoverEvent.POPOVER_DESTROYED, self.__handlerDestroyPopover)
        super(PopoverManager, self).destroy()

    def __handlerDestroyPopover(self, _):
        self.as_onPopoverDestroyS()