# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/main_wnd_state_watcher.py
import BigWorld

class ClientMainWindowStateWatcher(object):

    def __init__(self):
        self.__callbackID = None
        self.__isWindowVisible = True
        return

    def mainWindowWatcherInit(self):
        self.__clear()
        self.__isWindowVisible = BigWorld.isWindowVisible()
        self.__tick()

    def mainWindowWatcherDestroy(self):
        self.__clear()

    def __clear(self):
        if self.__callbackID is not None:
            BigWorld.cancelCallback(self.__callbackID)
            self.__callbackID = None
        return

    def __tick(self):
        self.__callbackID = None
        self.__onTick()
        self.__callbackID = BigWorld.callback(0.0, self.__tick)
        return

    def __onTick(self):
        isWindowVisible = BigWorld.isWindowVisible()
        if isWindowVisible != self.__isWindowVisible:
            self.__isWindowVisible = isWindowVisible
            self._onClientMainWindowStateChanged(isWindowVisible)

    def _onClientMainWindowStateChanged(self, isWindowVisible):
        pass