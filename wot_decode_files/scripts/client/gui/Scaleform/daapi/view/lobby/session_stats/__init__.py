# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/session_stats/__init__.py
from frameworks.wulf import WindowLayer
from gui.Scaleform.daapi.view.lobby.session_stats.session_stats_popover import SessionStatsPopover
from gui.Scaleform.daapi.view.lobby.session_stats.session_stats_settings import SessionStatsSettings
from gui.Scaleform.framework import ComponentSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.Scaleform.genConsts.SESSION_STATS_CONSTANTS import SESSION_STATS_CONSTANTS
from gui.app_loader import settings as app_settings
from gui.shared.event_bus import EVENT_BUS_SCOPE

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.session_stats.session_stats_overview import SessionStatsOverview
    from gui.Scaleform.daapi.view.lobby.session_stats.session_stats_views import SessionBattleStatsView
    from gui.Scaleform.daapi.view.lobby.session_stats.session_stats_views import SessionVehicleStatsView
    from gui.Scaleform.framework import GroupedViewSettings
    from gui.Scaleform.framework import ScopeTemplates
    return (
     ComponentSettings(SESSION_STATS_CONSTANTS.SESSION_BATTLE_STATS_VIEW_PY_ALIAS, SessionBattleStatsView, ScopeTemplates.VIEW_SCOPE),
     ComponentSettings(SESSION_STATS_CONSTANTS.SESSION_VEHICLE_STATS_VIEW_PY_ALIAS, SessionVehicleStatsView, ScopeTemplates.VIEW_SCOPE),
     ComponentSettings(SESSION_STATS_CONSTANTS.SESSION_STATS_OVERVIEW_PY_ALIAS, SessionStatsOverview, ScopeTemplates.VIEW_SCOPE),
     ComponentSettings(SESSION_STATS_CONSTANTS.SESSION_STATS_SETTINGS_PY_ALIAS, SessionStatsSettings, ScopeTemplates.VIEW_SCOPE),
     GroupedViewSettings(SESSION_STATS_CONSTANTS.SESSION_STATS_POPOVER, SessionStatsPopover, 'sessionStatsPopover.swf', WindowLayer.WINDOW, 'SessionStatsPopover', SESSION_STATS_CONSTANTS.SESSION_STATS_POPOVER, ScopeTemplates.WINDOW_VIEWED_MULTISCOPE))


def getBusinessHandlers():
    return (
     SessionStatsPackageBusinessHandler(),)


class SessionStatsPackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          SESSION_STATS_CONSTANTS.SESSION_STATS_POPOVER, self.loadViewByCtxEvent),)
        super(SessionStatsPackageBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)