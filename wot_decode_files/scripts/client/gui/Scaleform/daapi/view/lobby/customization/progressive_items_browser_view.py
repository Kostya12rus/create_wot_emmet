# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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