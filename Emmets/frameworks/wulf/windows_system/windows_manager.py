# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/frameworks/wulf/windows_system/windows_manager.py
import logging, typing, Event
from ..py_object_binder import PyObjectEntity
from .windows_area import WindowsArea
_logger = logging.getLogger(__name__)

class WindowsManager(PyObjectEntity):
    __slots__ = ('__eManager', 'onWindowStatusChanged', 'onViewStatusChanged', '__weakref__')

    def __init__(self, cppObject=None):
        super(WindowsManager, self).__init__(cppObject)
        self.__eManager = Event.EventManager()
        self.onWindowStatusChanged = Event.Event(self.__eManager)
        self.onViewStatusChanged = Event.Event(self.__eManager)

    @classmethod
    def create(cls, proxy):
        vm = WindowsManager()
        vm.bind(proxy)
        return vm

    def destroy(self):
        self.__eManager.clear()
        if self.proxy is not None:
            self.proxy.pyClear()
        self.unbind()
        return

    def getView(self, uniqueID):
        return self.proxy.getPyView(int(uniqueID))

    def getViewsByLayout(self, layoutID):
        return self.proxy.getPyViewsByLayoutId(layoutID)

    def getViewByLayoutID(self, layoutID):
        views = self.proxy.getPyViewsByLayoutId(layoutID)
        if len(views) > 1:
            _logger.warning('There are more than one view loaded with layoutID = %s', layoutID)
        if not views:
            return None
        else:
            return views[0]

    def getWindow(self, uniqueID):
        return self.proxy.getPyWindow(uniqueID)

    def findWindows(self, predicate):
        return self.proxy.findPyWindows(predicate)

    def findViews(self, predicate):
        return self.proxy.findPyViews(predicate)

    def addWindowsArea(self, areaID):
        area = WindowsArea()
        if self.proxy.addPyWindowsArea(areaID, area.proxy):
            return area
        else:
            area.unbind()
            return

    def removeWindowsArea(self, areaID):
        return self.proxy.removePyWindowsArea(areaID)

    def getWindowsArea(self, areaID):
        return self.proxy.getPyWindowsArea(areaID)

    def loadView(self, layoutID, viewClass, *args, **kwargs):
        pyView = self.getView(layoutID)
        if pyView is None:
            pyView = viewClass(layoutID, *args, **kwargs)
            pyView.load()
        else:
            _logger.warning('View is already loading/loaded: %r.', layoutID)
        return pyView

    def _cWindowStatusChangedEvent(self, uniqueID, newStatus):
        self.onWindowStatusChanged(uniqueID, newStatus)

    def _cViewStatusChangedEvent(self, uniqueID, newStatus):
        self.onViewStatusChanged(uniqueID, newStatus)