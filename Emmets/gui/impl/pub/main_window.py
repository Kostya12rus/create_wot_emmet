# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/pub/main_window.py
from frameworks.wulf import WindowFlags
from gui.impl.gen import R
from gui.impl.pub.window_impl import WindowImpl

class MainWindow(WindowImpl):
    __slots__ = ()

    def __init__(self, entryID, content=None):
        super(MainWindow, self).__init__(WindowFlags.MAIN_WINDOW, entryID=entryID, content=content)

    def _initialize(self):
        super(MainWindow, self)._initialize()
        self.gui.windowsManager.addWindowsArea(R.areas.default())
        self.gui.windowsManager.addWindowsArea(R.areas.specific())
        self.gui.windowsManager.addWindowsArea(R.areas.pop_over())
        self.gui.windowsManager.addWindowsArea(R.areas.context_menu())

    def _finalize(self):
        self.gui.windowsManager.removeWindowsArea(R.areas.default())
        self.gui.windowsManager.removeWindowsArea(R.areas.specific())
        self.gui.windowsManager.removeWindowsArea(R.areas.pop_over())
        self.gui.windowsManager.removeWindowsArea(R.areas.context_menu())
        super(MainWindow, self)._finalize()