# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/ClientSelectableWebLinksOpener.py
from ClientSelectableObject import ClientSelectableObject
from gui.shared import g_eventBus, events

class ClientSelectableWebLinksOpener(ClientSelectableObject):

    def onMouseClick(self):
        super(ClientSelectableWebLinksOpener, self).onMouseClick()
        if self.url:
            g_eventBus.handleEvent(events.OpenLinkEvent(events.OpenLinkEvent.PARSED, url=self.url))