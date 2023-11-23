# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/auxiliary/tooltips/simple_tooltip.py
from gui.impl.backport.backport_tooltip import DecoratedTooltipWindow
from gui.impl.gen import R
from gui.impl.pub.tooltip_window import SimpleTooltipContent

def createSimpleTooltip(parent, event, header='', body=''):
    window = DecoratedTooltipWindow(parent=parent, content=SimpleTooltipContent(R.views.common.tooltip_window.simple_tooltip_content.SimpleTooltipContent(), body=body, header=header))
    window.load()
    window.move(event.mouse.positionX, event.mouse.positionY)
    return window