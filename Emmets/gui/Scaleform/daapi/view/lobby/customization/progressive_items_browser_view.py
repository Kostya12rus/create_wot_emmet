# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/customization/progressive_items_browser_view.py
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebView
from gui.server_events.pm_constants import SOUNDS

class ProgressiveItemsBrowserView(WebView):

    def onCloseView(self):
        super(ProgressiveItemsBrowserView, self)._dispose()

    def _populate(self):
        super(ProgressiveItemsBrowserView, self)._populate()
        self.soundManager.setRTPC(SOUNDS.RTCP_OVERLAY, SOUNDS.MAX_MISSIONS_ZOOM)

    def _dispose(self):
        self.soundManager.setRTPC(SOUNDS.RTCP_OVERLAY, SOUNDS.MIN_MISSIONS_ZOOM)
        super(ProgressiveItemsBrowserView, self)._dispose()