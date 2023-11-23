# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/common/view_wrappers.py
from functools import wraps
from gui.impl import backport
from gui.impl.gen import R

def createBackportTooltipDecorator():

    def decorator(method):

        @wraps(method)
        def wrapper(self, event, *args, **kwargs):
            if event.contentID != R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
                return method(self, event, *args, **kwargs)
            else:
                tooltipData = self.getTooltipData(event)
                if tooltipData is None:
                    return
                window = backport.BackportTooltipWindow(tooltipData, self.getParentWindow())
                if window is None:
                    return
                window.load()
                return window

        return wrapper

    return decorator