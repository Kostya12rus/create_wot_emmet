# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/browser.py
import logging, typing
from web.client_web_api.common import WebEventSender
from web.web_client_api import WebCommandHandler
if typing.TYPE_CHECKING:
    from WebBrowser import WebBrowser
_logger = logging.getLogger(__name__)

class BrowserViewWebHandlers(object):
    __slots__ = ('__webCommandHandler', '__webEventSender', '__browser')

    def __init__(self, browser, browserID, view, webHandlersMap=None, alias=''):
        super(BrowserViewWebHandlers, self).__init__()
        self.__browser = browser
        self.__webCommandHandler = WebCommandHandler(browserID, alias, view)
        if webHandlersMap is not None:
            self.__webCommandHandler.addHandlers(webHandlersMap)
        self.__webCommandHandler.onCallback += self.__onWebCommandCallback
        self.__webEventSender = WebEventSender()
        self.__webEventSender.onCallback += self.__onWebEventCallback
        self.__webEventSender.init()
        return

    def fini(self):
        if self.__webCommandHandler:
            self.__webCommandHandler.fini()
            self.__webCommandHandler = None
        if self.__webEventSender:
            self.__webEventSender.fini()
            self.__webEventSender = None
        return

    def handleCommand(self, command):
        try:
            if self.__webCommandHandler is not None:
                self.__webCommandHandler.handleCommand(command)
        except Exception as e:
            _logger.exception(e)

        return

    def __onWebCommandCallback(self, callbackData):
        self.__browser.sendMessage(callbackData)

    def __onWebEventCallback(self, callbackData):
        self.__browser.sendEvent(callbackData)