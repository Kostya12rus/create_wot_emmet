# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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