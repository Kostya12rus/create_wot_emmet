# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/battle_pass/battle_pass_video_browser_view.py
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebView
from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE

class BattlePassVideoBrowserView(WebView):

    def _dispose(self):
        g_eventBus.handleEvent(events.BattlePassEvent(events.BattlePassEvent.VIDEO_SHOWN), scope=EVENT_BUS_SCOPE.LOBBY)
        super(BattlePassVideoBrowserView, self)._dispose()