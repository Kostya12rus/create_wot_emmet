# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_control/ChinaController.py
from adisp import adisp_process
from gui.Scaleform.locale.MENU import MENU
from helpers import dependency
from skeletons.gui.game_control import IBrowserController, IChinaController, IGameSessionController

class NoChinaController(IChinaController):

    def showBrowser(self):
        pass


class ChinaController(IChinaController):
    gameSession = dependency.descriptor(IGameSessionController)
    browser = dependency.descriptor(IBrowserController)

    def __init__(self):
        super(ChinaController, self).__init__()
        self.__browserID = None
        return

    def onDisconnected(self):
        if self.__browserID is not None:
            self.__browserClosed(self.__browserID)
        return

    @adisp_process
    def showBrowser(self):
        self.__browserID = yield self.browser.load(title=MENU.BROWSER_WINDOW_TITLE, browserID=self.__browserID)
        self.browser.onBrowserDeleted += self.__browserClosed

    def __browserClosed(self, browserId):
        if browserId == self.__browserID:
            self.__browserID = None
            self.browser.onBrowserDeleted -= self.__browserClosed
        return