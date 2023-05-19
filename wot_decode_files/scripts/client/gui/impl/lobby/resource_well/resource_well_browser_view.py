# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/resource_well/resource_well_browser_view.py
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebView
from gui.sounds.filters import switchHangarFilteredFilter

class ResourceWellBrowserView(WebView):

    def _populate(self):
        super(ResourceWellBrowserView, self)._populate()
        switchHangarFilteredFilter(on=True)

    def _dispose(self):
        switchHangarFilteredFilter(on=False)
        super(ResourceWellBrowserView, self)._dispose()