# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/missions/personal/__init__.py
from operator import methodcaller
from frameworks.wulf import WindowLayer
from gui.Scaleform.Waiting import Waiting
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.missions.personal.personal_missions_first_entry_award_view import PersonalMissionFirstEntryAwardView
from gui.Scaleform.daapi.view.lobby.missions.personal.personal_missions_first_entry_view import PersonalMissionFirstEntryView
from gui.Scaleform.daapi.view.lobby.missions.personal.tank_girls_popover import TankgirlsPopover
from gui.Scaleform.framework import ViewSettings, ScopeTemplates, GroupedViewSettings, ComponentSettings
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.Scaleform.genConsts.PERSONAL_MISSIONS_ALIASES import PERSONAL_MISSIONS_ALIASES
from gui.app_loader import settings as app_settings
from gui.server_events.pm_constants import PM_TUTOR_FIELDS
from gui.shared import EVENT_BUS_SCOPE
from gui.shared.events import LoadViewEvent
from helpers import dependency
from shared_utils import findFirst
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.server_events import IEventsCache

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.missions.personal.personal_missions_map_view import PersonalMissionsMapView
    from gui.Scaleform.daapi.view.lobby.missions.personal.personal_missions_page import PersonalMissionsPage
    from gui.Scaleform.daapi.view.lobby.missions.personal.personal_missions_operation_awards_screen import PersonalMissionsOperationAwardsScreen
    from gui.Scaleform.daapi.view.lobby.missions.personal.personal_missions_awards_view import PersonalMissionsAwardsView
    from gui.Scaleform.daapi.view.lobby.missions.personal.personal_missions_details_container_view import PersonalMissionDetailsContainerView
    from gui.Scaleform.daapi.view.lobby.missions.personal.free_sheet_popover import FreeSheetPopover
    from gui.Scaleform.daapi.view.lobby.missions.personal.personal_missions_operations import PersonalMissionOperations
    from gui.Scaleform.daapi.view.lobby.missions.personal.personal_missions_quest_award_screen import PersonalMissionsQuestAwardScreen
    from gui.Scaleform.daapi.view.lobby.missions.personal.personal_missions_browser_view import PersonalMissionsBrowserView
    return (
     ViewSettings(VIEW_ALIAS.LOBBY_PERSONAL_MISSIONS, PersonalMissionOperations, 'personalMissionsOperations.swf', WindowLayer.SUB_VIEW, VIEW_ALIAS.LOBBY_PERSONAL_MISSIONS, ScopeTemplates.LOBBY_SUB_SCOPE),
     ViewSettings(PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_PAGE_ALIAS, PersonalMissionsPage, 'personalMissionsPage.swf', WindowLayer.SUB_VIEW, PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_PAGE_ALIAS, ScopeTemplates.LOBBY_SUB_SCOPE),
     ViewSettings(PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_OPERATION_AWARDS_SCREEN_ALIAS, PersonalMissionsOperationAwardsScreen, 'personalMissionAwardsScreen.swf', WindowLayer.FULLSCREEN_WINDOW, PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_OPERATION_AWARDS_SCREEN_ALIAS, ScopeTemplates.LOBBY_TOP_SUB_SCOPE, True),
     ComponentSettings(PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_MAP_VIEW_ALIAS, PersonalMissionsMapView, ScopeTemplates.VIEW_SCOPE),
     ViewSettings(PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_AWARDS_VIEW_ALIAS, PersonalMissionsAwardsView, 'personalMissionsAwardsView.swf', WindowLayer.SUB_VIEW, PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_AWARDS_VIEW_ALIAS, ScopeTemplates.LOBBY_SUB_SCOPE),
     ViewSettings(PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSION_FIRST_ENTRY_VIEW_ALIAS, PersonalMissionFirstEntryView, 'personalMissionFirstEntryView.swf', WindowLayer.SUB_VIEW, PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSION_FIRST_ENTRY_VIEW_ALIAS, ScopeTemplates.LOBBY_SUB_SCOPE),
     ViewSettings(VIEW_ALIAS.LOBBY_PERSONAL_MISSION_DETAILS, PersonalMissionDetailsContainerView, 'personalMissionDetails.swf', WindowLayer.TOP_SUB_VIEW, VIEW_ALIAS.LOBBY_PERSONAL_MISSION_DETAILS, ScopeTemplates.LOBBY_SUB_SCOPE, True),
     ViewSettings(PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSION_FIRST_ENTRY_AWARD_VIEW_ALIAS, PersonalMissionFirstEntryAwardView, 'personalMissionFirstEntryAwardView.swf', WindowLayer.SUB_VIEW, PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSION_FIRST_ENTRY_AWARD_VIEW_ALIAS, ScopeTemplates.LOBBY_SUB_SCOPE),
     GroupedViewSettings(PERSONAL_MISSIONS_ALIASES.FREE_SHEET_POPOVER, FreeSheetPopover, 'freeSheetPopoverView.swf', WindowLayer.WINDOW, PERSONAL_MISSIONS_ALIASES.FREE_SHEET_POPOVER, PERSONAL_MISSIONS_ALIASES.FREE_SHEET_POPOVER, ScopeTemplates.LOBBY_SUB_SCOPE),
     GroupedViewSettings(PERSONAL_MISSIONS_ALIASES.TANK_GIRLS_POPOVER, TankgirlsPopover, 'tankgirlsPopoverView.swf', WindowLayer.WINDOW, PERSONAL_MISSIONS_ALIASES.TANK_GIRLS_POPOVER, PERSONAL_MISSIONS_ALIASES.TANK_GIRLS_POPOVER, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_QUEST_AWARD_SCREEN_ALIAS, PersonalMissionsQuestAwardScreen, 'personalMissionsQuestAwardScreen.swf', WindowLayer.FULLSCREEN_WINDOW, PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_QUEST_AWARD_SCREEN_ALIAS, ScopeTemplates.LOBBY_TOP_SUB_SCOPE, True),
     ViewSettings(PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSION_BROWSER_VIEW_ALIAS, PersonalMissionsBrowserView, 'browserScreen.swf', WindowLayer.SUB_VIEW, PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSION_BROWSER_VIEW_ALIAS, ScopeTemplates.LOBBY_SUB_SCOPE, True))


def getBusinessHandlers():
    return (
     PersonalMissionsPackageBusinessHandler(),)


class PersonalMissionsPackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          VIEW_ALIAS.LOBBY_PERSONAL_MISSIONS, self.loadPersonalMissionsView),
         (
          VIEW_ALIAS.LOBBY_PERSONAL_MISSION_DETAILS, self.loadViewByCtxEvent),
         (
          PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_OPERATIONS_PAGE_ALIAS, self.loadPersonalMissionsView),
         (
          PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS2_OPERATIONS_PAGE_ALIAS, self.loadPersonalMissionsView),
         (
          PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_PAGE_ALIAS, self.loadPersonalMissionsView),
         (
          PERSONAL_MISSIONS_ALIASES.FREE_SHEET_POPOVER, self.loadViewByCtxEvent),
         (
          PERSONAL_MISSIONS_ALIASES.TANK_GIRLS_POPOVER, self.loadViewByCtxEvent),
         (
          PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_AWARDS_VIEW_ALIAS, self.loadAwardsView),
         (
          PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSION_FIRST_ENTRY_VIEW_ALIAS, self.loadViewByCtxEvent),
         (
          PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSION_FIRST_ENTRY_AWARD_VIEW_ALIAS, self.loadViewByCtxEvent),
         (
          PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_QUEST_AWARD_SCREEN_ALIAS, self.loadViewByCtxEvent),
         (
          PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_OPERATION_AWARDS_SCREEN_ALIAS, self.loadViewByCtxEvent),
         (
          PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSION_BROWSER_VIEW_ALIAS, self.loadViewByCtxEvent))
        super(PersonalMissionsPackageBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)

    def loadAwardsView(self, event):
        preloadOperationsPage = event.ctx.get('isBackEvent')
        if preloadOperationsPage:
            Waiting.show('loadPage')
            self.loadViewByCtxEvent(LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.LOBBY_PERSONAL_MISSIONS), ctx=event.ctx))
        self.loadViewByCtxEvent(event)
        if preloadOperationsPage:
            Waiting.hide('loadPage')

    def loadPersonalMissionsView(self, event):
        settingsCore = dependency.instance(ISettingsCore)
        eventsCache = dependency.instance(IEventsCache)
        uiStorage = settingsCore.serverSettings.getUIStorage()
        goByDefault = True
        if not uiStorage.get(PM_TUTOR_FIELDS.GREETING_SCREEN_SHOWN):
            self.loadViewByCtxEvent(LoadViewEvent(SFViewLoadParams(PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSION_FIRST_ENTRY_VIEW_ALIAS), ctx=event.ctx))
            goByDefault = False
        elif not uiStorage.get(PM_TUTOR_FIELDS.FIRST_ENTRY_AWARDS_SHOWN):
            if findFirst(methodcaller('isAwardAchieved'), eventsCache.getPersonalMissions().getAllOperations().values()):
                self.loadViewByCtxEvent(LoadViewEvent(SFViewLoadParams(PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSION_FIRST_ENTRY_AWARD_VIEW_ALIAS), ctx=event.ctx))
                goByDefault = False
            else:
                settingsCore.serverSettings.saveInUIStorage({PM_TUTOR_FIELDS.FIRST_ENTRY_AWARDS_SHOWN: True})
        if goByDefault:
            if event.alias == VIEW_ALIAS.LOBBY_PERSONAL_MISSIONS:
                self.loadViewByCtxEvent(LoadViewEvent(SFViewLoadParams(PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_OPERATIONS), ctx=event.ctx))
            else:
                self.loadViewByCtxEvent(event)