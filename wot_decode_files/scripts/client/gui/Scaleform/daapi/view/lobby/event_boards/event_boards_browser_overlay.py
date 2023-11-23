# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_boards_browser_overlay.py
from gui.Scaleform.daapi.view.lobby.event_boards.browser_in_view_component import BrowserInViewComponent

class EventBoardsBrowserOverlay(BrowserInViewComponent):

    def setOpener(self, view):
        self.setUrl(view.ctx.get('url'))
        self.as_setTitleS(view.ctx.get('title'))