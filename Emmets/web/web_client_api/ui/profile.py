# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/profile.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import events, g_eventBus, showProfileWindow, requestProfile
from web.web_client_api import w2c, W2CSchema, Field

class _OpenProfileWindowSchema(W2CSchema):
    database_id = Field(required=True, type=(int, long))
    user_name = Field(required=True, type=basestring)


_PROFILE_TAB_ALIASES = {'hof': VIEW_ALIAS.PROFILE_HOF, 
   'technique': VIEW_ALIAS.PROFILE_TECHNIQUE_PAGE, 
   'summary': VIEW_ALIAS.PROFILE_SUMMARY_PAGE, 
   'awards': VIEW_ALIAS.PROFILE_AWARDS, 
   'statistics': VIEW_ALIAS.PROFILE_STATISTICS}

class _OpenProfileTabSchema(W2CSchema):
    selected_id = Field(type=basestring, validator=(lambda value, data: value in _PROFILE_TAB_ALIASES))


class ProfileTabWebApiMixin(object):

    @w2c(_OpenProfileTabSchema, 'profile')
    def profile(self, cmd):
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.LOBBY_PROFILE), ctx={'selectedAlias': _PROFILE_TAB_ALIASES[cmd.selected_id]} if cmd.selected_id else None), scope=EVENT_BUS_SCOPE.LOBBY)
        return


class ProfileWindowWebApiMixin(object):

    @w2c(_OpenProfileWindowSchema, 'profile_window')
    def profile(self, cmd):

        def onDossierReceived(databaseID, userName):
            showProfileWindow(databaseID, userName)

        requestProfile(cmd.database_id, cmd.user_name, successCallback=onDossierReceived)