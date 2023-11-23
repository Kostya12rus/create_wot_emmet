# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/common/view_mixins.py
from gui.Scaleform.daapi.view.lobby.header.LobbyHeader import HeaderMenuVisibilityState
from gui.shared import events, g_eventBus, EVENT_BUS_SCOPE

class LobbyHeaderVisibility(object):
    __slots__ = ()

    @classmethod
    def suspendLobbyHeader(cls, state=HeaderMenuVisibilityState.NOTHING):
        cls._toggleLobbyHeaderVisibility(state)

    @classmethod
    def resumeLobbyHeader(cls, state=HeaderMenuVisibilityState.ALL):
        cls._toggleLobbyHeaderVisibility(state)

    @classmethod
    def _toggleLobbyHeaderVisibility(cls, state):
        event = events.LobbyHeaderMenuEvent(events.LobbyHeaderMenuEvent.TOGGLE_VISIBILITY, ctx={'state': state})
        g_eventBus.handleEvent(event, EVENT_BUS_SCOPE.LOBBY)