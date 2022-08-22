# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/resource_well/resource_well_browser_view.py
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebView, WebViewTransparent
from gui.sounds.filters import switchHangarFilteredFilter
from uilogging.resource_well.loggers import ResourceWellInfoScreenLogger, ResourceWellIntroVideoLogger

class ResourceWellBrowserView(WebView):
    __uiLogger = ResourceWellInfoScreenLogger()

    def _populate(self):
        super(ResourceWellBrowserView, self)._populate()
        switchHangarFilteredFilter(on=True)
        self.__uiLogger.onViewOpened()

    def _dispose(self):
        switchHangarFilteredFilter(on=False)
        self.__uiLogger.onViewClosed()
        super(ResourceWellBrowserView, self)._dispose()


class ResourceWellVideoView(WebViewTransparent):
    __uiLogger = ResourceWellIntroVideoLogger()

    def _populate(self):
        super(ResourceWellVideoView, self)._populate()
        self.__uiLogger.onViewOpened()

    def _dispose(self):
        self.__uiLogger.onViewClosed()
        super(ResourceWellVideoView, self)._dispose()