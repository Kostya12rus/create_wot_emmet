# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/AbstractPopOverView.py
from gui.Scaleform.daapi.view.meta.PopOverViewMeta import PopOverViewMeta
from gui.shared.events import HidePopoverEvent

class AbstractPopOverView(PopOverViewMeta):

    def __init__(self, ctx=None):
        super(AbstractPopOverView, self).__init__()

    def _populate(self):
        super(AbstractPopOverView, self)._populate()
        self.addListener(HidePopoverEvent.HIDE_POPOVER, self._handlerHidePopover)

    def _handlerHidePopover(self, event):
        self.destroy()

    def _dispose(self):
        self.removeListener(HidePopoverEvent.HIDE_POPOVER, self._handlerHidePopover)
        super(AbstractPopOverView, self)._dispose()
        self.fireEvent(HidePopoverEvent(HidePopoverEvent.POPOVER_DESTROYED))