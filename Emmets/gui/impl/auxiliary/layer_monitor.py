# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/auxiliary/layer_monitor.py
import weakref, logging
from frameworks.wulf import ViewStatus
from helpers import dependency
from skeletons.gui.impl import IGuiLoader
_logger = logging.getLogger(__name__)

class LayerMonitor(object):
    __gui = dependency.descriptor(IGuiLoader)

    def __init__(self):
        self.__window = None
        return

    def init(self, cls):
        self.__gui.windowsManager.onWindowStatusChanged += self.__windowStatusChanged
        self.__window = weakref.proxy(cls)

    def fini(self):
        self.__gui.windowsManager.onWindowStatusChanged -= self.__windowStatusChanged
        self.__window = None
        return

    def __windowStatusChanged(self, uniqueID, newStatus):
        if newStatus == ViewStatus.LOADED:
            window = self.__gui.windowsManager.getWindow(uniqueID)
            if window.layer == self.__window.layer and window.uniqueID != self.__window.uniqueID:
                self.__window.destroy()
                _logger.info('Window %r has been destroyed by opening window %r', self.__window, window)