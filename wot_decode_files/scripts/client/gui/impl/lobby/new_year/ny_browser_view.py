# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/new_year/ny_browser_view.py
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebViewTransparent
from uilogging.ny.loggers import NyInfoVideoLogger

class NyBrowserView(WebViewTransparent):
    __uiLogger = NyInfoVideoLogger()

    def _populate(self):
        super(NyBrowserView, self)._populate()
        self.__uiLogger.onViewOpened()

    def _dispose(self):
        self.__uiLogger.onViewClosed()
        super(NyBrowserView, self)._dispose()