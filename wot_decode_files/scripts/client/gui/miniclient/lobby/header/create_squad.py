# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/miniclient/lobby/header/create_squad.py
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.shared.event_bus import EVENT_BUS_SCOPE
from helpers import aop
from gui.shared import events, g_eventBus
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS

class _OnCreateSquadClickAspect(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.SQUAD_PROMO_WINDOW)), EVENT_BUS_SCOPE.LOBBY)


class OnCreateSquadClickPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.header.LobbyHeader', 'LobbyHeader', 'showSquad', aspects=(
         _OnCreateSquadClickAspect,))