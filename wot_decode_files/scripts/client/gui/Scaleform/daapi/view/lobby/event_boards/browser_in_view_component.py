# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/browser_in_view_component.py
import BigWorld
from adisp import adisp_process
from debug_utils import LOG_ERROR
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from helpers import dependency
from gui.Scaleform.daapi.view.meta.BrowserInViewComponentMeta import BrowserInViewComponentMeta
from skeletons.gui.game_control import IBrowserController

class BrowserInViewComponent(BrowserInViewComponentMeta):
    browserCtrl = dependency.descriptor(IBrowserController)

    def __init__(self):
        super(BrowserInViewComponent, self).__init__()
        self.__browserId = None
        self.__url = None
        self.__size = None
        self.__browserViewCreated = False
        return

    def viewSize(self, width, height):
        self.__size = (width, height)

    def setUrl(self, url):
        if self.__url == url:
            return
        self.__url = url
        self.__loadBrowser()

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(BrowserInViewComponent, self)._onRegisterFlashComponent(viewPy, alias)
        if alias == VIEW_ALIAS.BROWSER:
            viewPy.init(self.__browserId)

    @adisp_process
    def __loadBrowser(self):
        url = self.__url
        width, height = self.__size
        self.__browserId = yield self.browserCtrl.load(url=url, useBrowserWindow=False, showBrowserCallback=self.__showBrowser, browserSize=(
         width, height))
        browser = self.browserCtrl.getBrowser(self.__browserId)
        if browser:
            browser.useSpecialKeys = False
            browser.allowRightClick = False
        else:
            LOG_ERROR('Failed to create browser!')

    def __showBrowser(self):
        if not self.__browserViewCreated:
            BigWorld.callback(0.01, self.as_loadBrowserS)
            self.__browserViewCreated = True