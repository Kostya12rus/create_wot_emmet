# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/miniclient/lobby/strongholds/aspects.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from helpers import aop
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS

class MakeStrongholdsUnavailable(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        tooltip = TOOLTIPS.HEADER_BUTTONS_FORTS_SANDBOX_TURNEDOFF
        return {'label': MENU.HEADERBUTTONS_CLAN, 
           'value': VIEW_ALIAS.LOBBY_STRONGHOLD, 
           'tooltip': tooltip, 
           'enabled': False}