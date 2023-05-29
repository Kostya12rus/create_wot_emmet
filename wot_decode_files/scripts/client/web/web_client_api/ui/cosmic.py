# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/cosmic.py
from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
from web.web_client_api import W2CSchema, w2c

class CosmicEventLobbyWebApiMixin(object):

    @w2c(W2CSchema, 'cosmic_lobby')
    def openCosmicLobbyView(self, _):
        g_eventBus.handleEvent(events.CosmicEvent(events.CosmicEvent.OPEN_COSMIC), scope=EVENT_BUS_SCOPE.LOBBY)