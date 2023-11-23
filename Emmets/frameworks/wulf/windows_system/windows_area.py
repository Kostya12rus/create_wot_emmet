# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/frameworks/wulf/windows_system/windows_area.py
import typing
from .window import Window
from ..gui_constants import PositionAnchor
from ..py_object_binder import PyObjectEntity
from ..py_object_wrappers import PyObjectWindowsArea

class WindowsArea(PyObjectEntity):
    __slots__ = ()

    def __init__(self):
        super(WindowsArea, self).__init__(cppObject=PyObjectWindowsArea())

    @property
    def areaID(self):
        proxy = self.proxy
        if proxy is not None:
            return proxy.areaID
        else:
            return 0

    def addWindow(self, window):
        return self.proxy.addPyWindow(window.proxy)

    def removeWindow(self, window):
        return self.proxy.removePyWindow(window.proxy)

    def getFirstWindow(self):
        return self.proxy.getFirstPyWindow()

    def getLastWindow(self):
        return self.proxy.getLastPyWindow()

    def getPreviousNeighbor(self, window):
        return self.proxy.getPreviousPyNeighbor(window.uniqueID)

    def getNextNeighbor(self, window):
        return self.proxy.getNextPyNeighbor(window.uniqueID)

    def move(self, window, x, y, xAnchor=PositionAnchor.LEFT, yAnchor=PositionAnchor.TOP):
        return self.proxy.movePyWindow(window.uniqueID, x, y, xAnchor, yAnchor)

    def center(self, window):
        return self.proxy.centerPyWindow(window.uniqueID)

    def cascade(self, window):
        return self.proxy.cascadePyWindow(window.uniqueID)