# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/clan.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.shared.event_dispatcher import showClanProfileWindow, showClanInvitesWindow, showClanSearchWindow, showClanPersonalInvitesWindow, showBrowserOverlayView
from web.web_client_api import w2c, W2CSchema, Field

class _OpenBrowserOverlaySchema(W2CSchema):
    url = Field(required=True, type=basestring)


class _OpenClanCardSchema(W2CSchema):
    clan_dbid = Field(required=True, type=(int, long))
    clan_abbrev = Field(required=True, type=basestring)


class ClanWindowWebApiMixin(object):

    @w2c(_OpenClanCardSchema, 'clan_card_window')
    def clanCardWindow(self, cmd):
        showClanProfileWindow(cmd.clan_dbid, cmd.clan_abbrev)

    @w2c(W2CSchema, 'clan_invites_window')
    def handleOpenClanInvites(self, cmd):
        showClanInvitesWindow()

    @w2c(W2CSchema, 'clan_search_window')
    def handleOpenClanSearch(self, cmd):
        showClanSearchWindow()

    @w2c(W2CSchema, 'clan_personal_invites_window')
    def handleOpenPersonalInvites(self, cmd):
        showClanPersonalInvitesWindow()

    @w2c(_OpenBrowserOverlaySchema, name='clan_ads_overlay')
    def handleOpenClanAds(self, cmd):
        showBrowserOverlayView(cmd.url, alias=VIEW_ALIAS.STRONGHOLD_ADS)