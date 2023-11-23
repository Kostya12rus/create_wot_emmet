# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/miniclient/contacts.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.shared import events, g_eventBus, EVENT_BUS_SCOPE
from helpers import aop

class _CreateSquadAspect(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.SQUAD_PROMO_WINDOW)), scope=EVENT_BUS_SCOPE.LOBBY)


class CreateSquadPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.user_cm_handlers', 'BaseUserCMHandler', 'createSquad', aspects=(
         _CreateSquadAspect,))