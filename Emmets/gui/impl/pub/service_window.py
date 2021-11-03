# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/pub/service_window.py
from frameworks.wulf import WindowFlags
from gui.impl.pub.window_impl import WindowImpl
from gui.impl.pub.window_view import WindowView

class ServiceWindow(WindowImpl):
    __slots__ = ()

    def __init__(self, content=None, parent=None, areaID=0):
        super(ServiceWindow, self).__init__(wndFlags=WindowFlags.SERVICE_WINDOW, decorator=WindowView(), content=content, parent=parent, areaID=areaID)