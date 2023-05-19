# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/pub/service_window.py
from frameworks.wulf import WindowFlags
from gui.impl.pub.window_impl import WindowImpl
from gui.impl.pub.window_view import WindowView

class ServiceWindow(WindowImpl):
    __slots__ = ()

    def __init__(self, content=None, parent=None, areaID=0):
        super(ServiceWindow, self).__init__(wndFlags=WindowFlags.SERVICE_WINDOW, decorator=WindowView(), content=content, parent=parent, areaID=areaID)