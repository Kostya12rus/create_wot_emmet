# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/profile/__init__.py
from frameworks.wulf import WindowLayer
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ViewSettings, GroupedViewSettings, ScopeTemplates, ComponentSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE

def getContextMenuHandlers():
    from gui.Scaleform.daapi.view.lobby.profile import profile_cm_handlers
    return (
     (
      CONTEXT_MENU_HANDLER_TYPE.PROFILE_VEHICLE, profile_cm_handlers.ProfileVehicleCMHandler),)


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.profile.ProfileAwards import ProfileAwards
    from gui.Scaleform.daapi.view.lobby.profile.ProfilePage import ProfilePage
    from gui.Scaleform.daapi.view.lobby.profile.ProfileStatistics import ProfileStatistics
    from gui.Scaleform.daapi.view.lobby.profile.ProfileSummaryPage import ProfileSummaryPage
    from gui.Scaleform.daapi.view.lobby.profile.ProfileSummaryWindow import ProfileSummaryWindow
    from gui.Scaleform.daapi.view.lobby.profile.ProfileTabNavigator import ProfileTabNavigator
    from gui.Scaleform.daapi.view.lobby.profile.ProfileTechniquePage import ProfileTechniquePage
    from gui.Scaleform.daapi.view.lobby.profile.ProfileTechniqueWindow import ProfileTechniqueWindow
    from gui.Scaleform.daapi.view.lobby.profile.ProfileWindow import ProfileWindow
    from gui.Scaleform.daapi.view.lobby.profile.ProfileHof import ProfileHof
    return (
     ViewSettings(VIEW_ALIAS.LOBBY_PROFILE, ProfilePage, 'profile.swf', WindowLayer.SUB_VIEW, VIEW_ALIAS.LOBBY_PROFILE, ScopeTemplates.LOBBY_SUB_SCOPE),
     GroupedViewSettings(VIEW_ALIAS.PROFILE_WINDOW, ProfileWindow, 'profileWindow.swf', WindowLayer.WINDOW, 'profileWindow', None, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(VIEW_ALIAS.PROFILE_AWARDS, ProfileAwards, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(VIEW_ALIAS.PROFILE_STATISTICS, ProfileStatistics, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(VIEW_ALIAS.PROFILE_SUMMARY_PAGE, ProfileSummaryPage, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(VIEW_ALIAS.PROFILE_SUMMARY_WINDOW, ProfileSummaryWindow, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(VIEW_ALIAS.PROFILE_TAB_NAVIGATOR, ProfileTabNavigator, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(VIEW_ALIAS.PROFILE_TECHNIQUE_PAGE, ProfileTechniquePage, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(VIEW_ALIAS.PROFILE_TECHNIQUE_WINDOW, ProfileTechniqueWindow, ScopeTemplates.DEFAULT_SCOPE),
     ComponentSettings(VIEW_ALIAS.PROFILE_HOF, ProfileHof, ScopeTemplates.DEFAULT_SCOPE))


def getBusinessHandlers():
    return (
     ProfilePackageBusinessHandler(),)


class ProfilePackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          VIEW_ALIAS.LOBBY_PROFILE, self.loadViewByCtxEvent),
         (
          VIEW_ALIAS.PROFILE_WINDOW, self.loadViewByCtxEvent))
        super(ProfilePackageBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)