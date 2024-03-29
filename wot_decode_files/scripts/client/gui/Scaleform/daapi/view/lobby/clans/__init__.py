# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/clans/__init__.py
from frameworks.wulf import WindowLayer
from gui.Scaleform.framework import GroupedViewSettings, ScopeTemplates, ComponentSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.Scaleform.genConsts.CLANS_ALIASES import CLANS_ALIASES
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE
from gui.app_loader import settings as app_settings
from gui.shared.event_bus import EVENT_BUS_SCOPE

def getContextMenuHandlers():
    from gui.Scaleform.daapi.view.lobby.clans import clan_cm_handlers
    return (
     (
      CONTEXT_MENU_HANDLER_TYPE.BASE_CLAN, clan_cm_handlers.BaseClanCMHandler),)


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.clans.invites.ClanPersonalInvitesView import ClanPersonalInvitesView
    from gui.Scaleform.daapi.view.lobby.clans.invites.ClanPersonalInvitesWindow import ClanPersonalInvitesWindow
    from gui.Scaleform.daapi.view.lobby.clans.invites.ClanSendInvitesWindow import ClanSendInvitesWindow
    from gui.Scaleform.daapi.view.lobby.clans.profile.ClanProfileGlobalMapInfoView import ClanProfileGlobalMapInfoView
    from gui.Scaleform.daapi.view.lobby.clans.profile.ClanProfileGlobalMapPromoView import ClanProfileGlobalMapPromoView
    from gui.Scaleform.daapi.view.lobby.clans.search.ClanSearchInfo import ClanSearchInfo
    from gui.Scaleform.daapi.view.lobby.clans.search.ClanSearchWindow import ClanSearchWindow
    from gui.Scaleform.daapi.view.lobby.clans.profile.ClanProfileStrongholdsView import ClanProfileStrongholdsView
    from gui.Scaleform.daapi.view.lobby.clans.profile.ClanProfileGlobalMapView import ClanProfileGlobalMapView
    from gui.Scaleform.daapi.view.lobby.clans.invites.ClanInvitesView import ClanInvitesView
    from gui.Scaleform.daapi.view.lobby.clans.invites.ClanInvitesWindow import ClanInvitesWindow
    from gui.Scaleform.daapi.view.lobby.clans.profile.ClanProfileMainWindow import ClanProfileMainWindow
    from gui.Scaleform.daapi.view.lobby.clans.profile.ClanProfilePersonnelView import ClanProfilePersonnelView
    from gui.Scaleform.daapi.view.lobby.clans.invites.ClanRequestsView import ClanRequestsView
    from gui.Scaleform.daapi.view.lobby.clans.profile.ClanProfileSummaryView import ClanProfileSummaryView
    from gui.Scaleform.daapi.view.lobby.clans.profile.ClanProfileTableStatisticsView import ClanProfileTableStatisticsView
    return (
     GroupedViewSettings(CLANS_ALIASES.CLAN_PROFILE_MAIN_WINDOW_PY, ClanProfileMainWindow, CLANS_ALIASES.CLAN_PROFILE_MAIN_WINDOW_UI, WindowLayer.WINDOW, '', CLANS_ALIASES.CLAN_PROFILE_MAIN_WINDOW_PY, ScopeTemplates.DEFAULT_SCOPE, True),
     GroupedViewSettings(CLANS_ALIASES.CLAN_PROFILE_INVITES_WINDOW_PY, ClanInvitesWindow, 'clanInvitesWindow.swf', WindowLayer.WINDOW, CLANS_ALIASES.CLAN_PROFILE_INVITES_WINDOW_PY, None, ScopeTemplates.LOBBY_SUB_SCOPE),
     GroupedViewSettings(CLANS_ALIASES.CLAN_PROFILE_SEND_INVITES_WINDOW_PY, ClanSendInvitesWindow, 'sendInvitesWindow.swf', WindowLayer.WINDOW, '', CLANS_ALIASES.CLAN_PROFILE_SEND_INVITES_WINDOW_PY, ScopeTemplates.DEFAULT_SCOPE),
     GroupedViewSettings(CLANS_ALIASES.CLAN_PERSONAL_INVITES_WINDOW_PY, ClanPersonalInvitesWindow, CLANS_ALIASES.CLAN_PERSONAL_INVITES_WINDOW_UI, WindowLayer.WINDOW, CLANS_ALIASES.CLAN_PERSONAL_INVITES_WINDOW_PY, None, ScopeTemplates.LOBBY_SUB_SCOPE),
     ComponentSettings(CLANS_ALIASES.CLAN_PROFILE_SUMMARY_VIEW_ALIAS, ClanProfileSummaryView, ScopeTemplates.VIEW_SCOPE),
     ComponentSettings(CLANS_ALIASES.CLAN_PROFILE_PERSONNEL_VIEW_ALIAS, ClanProfilePersonnelView, ScopeTemplates.VIEW_SCOPE),
     ComponentSettings(CLANS_ALIASES.CLAN_PROFILE_STRONGHOLDS_VIEW_ALIAS, ClanProfileStrongholdsView, ScopeTemplates.VIEW_SCOPE),
     ComponentSettings(CLANS_ALIASES.CLAN_PROFILE_GLOBALMAP_VIEW_ALIAS, ClanProfileGlobalMapView, ScopeTemplates.VIEW_SCOPE),
     ComponentSettings(CLANS_ALIASES.CLAN_PROFILE_GLOBALMAP_PROMO_VIEW_ALIAS, ClanProfileGlobalMapPromoView, ScopeTemplates.VIEW_SCOPE),
     ComponentSettings(CLANS_ALIASES.CLAN_PROFILE_GLOBALMAP_INFO_VIEW_ALIAS, ClanProfileGlobalMapInfoView, ScopeTemplates.VIEW_SCOPE),
     ComponentSettings(CLANS_ALIASES.CLAN_PROFILE_REQUESTS_VIEW_ALIAS, ClanRequestsView, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(CLANS_ALIASES.CLAN_PROFILE_INVITES_VIEW_ALIAS, ClanInvitesView, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(CLANS_ALIASES.CLAN_PROFILE_TABLE_STATISTICS_VIEW_ALIAS, ClanProfileTableStatisticsView, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(CLANS_ALIASES.CLAN_PERSONAL_INVITES_VIEW_ALIAS, ClanPersonalInvitesView, ScopeTemplates.DEFAULT_SCOPE),
     GroupedViewSettings(CLANS_ALIASES.CLAN_SEARCH_WINDOW_PY, ClanSearchWindow, 'clanSearchWindow.swf', WindowLayer.WINDOW, CLANS_ALIASES.CLAN_SEARCH_WINDOW_PY, None, ScopeTemplates.LOBBY_SUB_SCOPE),
     ComponentSettings(CLANS_ALIASES.CLAN_SEARCH_INFO_PY, ClanSearchInfo, ScopeTemplates.DEFAULT_SCOPE))


def getBusinessHandlers():
    return (
     _ClanProfileBusinessHandler(),)


class _ClanProfileBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          CLANS_ALIASES.CLAN_PROFILE_MAIN_WINDOW_PY, self.loadViewByCtxEvent),
         (
          CLANS_ALIASES.CLAN_PROFILE_INVITES_WINDOW_PY, self.loadViewByCtxEvent),
         (
          CLANS_ALIASES.CLAN_PROFILE_SEND_INVITES_WINDOW_PY, self.loadViewByCtxEvent),
         (
          CLANS_ALIASES.CLAN_SEARCH_WINDOW_PY, self.loadViewByCtxEvent),
         (
          CLANS_ALIASES.CLAN_PERSONAL_INVITES_WINDOW_PY, self.loadViewByCtxEvent))
        super(_ClanProfileBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)