# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/common/browser_view.py
import typing
from frameworks.wulf import ViewFlags
from gui.impl import backport
from gui.impl.common.browser import Browser, BrowserSettings
from gui.impl.gen.view_models.views.browser_view_model import BrowserViewModel
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
from sound_gui_manager import CommonSoundSpaceSettings
from web.web_client_api import webApiCollection
BrowserViewSettings = typing.NamedTuple('BrowserViewSettings', (
 (
  'url', str),
 (
  'webHandlers', typing.Optional[webApiCollection]),
 (
  'isClosable', bool),
 (
  'useSpecialKeys', bool),
 (
  'allowRightClick', bool),
 (
  'viewFlags', int),
 (
  'restoreBackground', bool),
 (
  'waitingMessageID', int),
 (
  'disabledKeys', typing.Iterable[typing.Tuple[(str, bool, bool, bool, bool)]]),
 (
  'soundSpaceSettings', typing.Optional[CommonSoundSpaceSettings]),
 (
  'returnClb', typing.Optional[typing.Callable])))

def makeSettings(url, webHandlers=None, isClosable=False, useSpecialKeys=False, allowRightClick=False, viewFlags=ViewFlags.LOBBY_SUB_VIEW, restoreBackground=False, waitingMessageID=R.invalid(), disabledKeys=(), soundSpaceSettings=None, returnClb=None):
    return BrowserViewSettings(url, webHandlers, isClosable, useSpecialKeys, allowRightClick, viewFlags, restoreBackground, waitingMessageID, disabledKeys, soundSpaceSettings, returnClb)


class BrowserView(Browser[BrowserViewModel]):
    __slots__ = ('__settings', '__closedByUser', '__forceClosed', '__savedBackAlpha')
    __background_alpha__ = 1.0
    __appLoader = dependency.descriptor(IAppLoader)

    def __init__(self, layoutID, settings):
        BrowserView._COMMON_SOUND_SPACE = settings.soundSpaceSettings
        super(BrowserView, self).__init__(url=settings.url, settings=BrowserSettings(layoutID=layoutID, flags=settings.viewFlags, model=BrowserViewModel()), webHandlersMap=settings.webHandlers, preload=True)
        self.__settings = settings
        self.__closedByUser = False
        self.__forceClosed = False
        self.__savedBackAlpha = None
        if self.browser is not None:
            self.__setupBrowser()
        else:
            self.onBrowserObtained += self.__onBrowserObtained
        return

    def onCloseView(self):
        self.__forceClosed = True
        self.destroyWindow()

    def _onLoading(self, *args, **kwargs):
        super(BrowserView, self)._onLoading(*args, **kwargs)
        self.getViewModel().onClose += self.__onClose
        with self.getViewModel().transaction() as (model):
            model.setIsClosable(self.__settings.isClosable)
            if self.__settings.waitingMessageID != R.invalid():
                self.setWaitingMessage(backport.msgid(self.__settings.waitingMessageID))

    def _initialize(self, *args, **kwargs):
        super(BrowserView, self)._initialize(*args, **kwargs)
        app = self.__appLoader.getApp()
        if self.__settings.restoreBackground:
            self.__savedBackAlpha = app.getBackgroundAlpha()
        app.setBackgroundAlpha(self.__background_alpha__)

    def _finalize(self):
        self.getViewModel().onClose -= self.__onClose
        self.onBrowserObtained -= self.__onBrowserObtained
        returnCallback = self.__settings.returnClb
        if returnCallback is not None:
            returnCallback(byUser=self.__closedByUser, url=self.browser.url if self.browser else '', forceClosed=self.__forceClosed)
        if self.__settings.restoreBackground and self.__savedBackAlpha is not None:
            self.__appLoader.getApp().setBackgroundAlpha(self.__savedBackAlpha)
        super(BrowserView, self)._finalize()
        return

    def __onClose(self):
        self.__closedByUser = True
        self.onCloseView()

    def __setupBrowser(self):
        self.browser.useSpecialKeys = self.__settings.useSpecialKeys
        self.browser.allowRightClick = self.__settings.allowRightClick
        self.browser.setDisabledKeys(self.__settings.disabledKeys)

    def __onBrowserObtained(self, _):
        self.__setupBrowser()