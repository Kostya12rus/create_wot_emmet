# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/missions/linked_set/__init__.py
from frameworks.wulf import WindowLayer
from gui.Scaleform.daapi.view.lobby.missions.linked_set.linkedset_vehicle_list_popup import LinkedSetVehicleListPopup
from gui.Scaleform.framework import ViewSettings, ScopeTemplates, GroupedViewSettings, ComponentSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.Scaleform.genConsts.LINKEDSET_ALIASES import LINKEDSET_ALIASES
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.app_loader.settings import APP_NAME_SPACE
from gui.shared import EVENT_BUS_SCOPE

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.missions.linked_set.linkedset_details_container_view import LinkedSetDetailsView
    from gui.Scaleform.daapi.view.lobby.missions.linked_set.linkedset_details_overlay import LinkedSetDetailsOverlay
    from gui.Scaleform.daapi.view.lobby.missions.linked_set.linkedset_hints import LinkedSetHintsView
    return (
     ViewSettings(LINKEDSET_ALIASES.LINKED_SET_DETAILS_CONTAINER_VIEW, LinkedSetDetailsView, 'linkedSetDetails.swf', WindowLayer.TOP_SUB_VIEW, LINKEDSET_ALIASES.LINKED_SET_DETAILS_CONTAINER_VIEW, ScopeTemplates.LOBBY_SUB_SCOPE, True),
     ComponentSettings(LINKEDSET_ALIASES.LINKED_SET_DETAILS_VIEW_ALIAS, LinkedSetDetailsOverlay, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(VIEW_ALIAS.LINKEDSET_HINTS, LinkedSetHintsView, 'linkedSetHints.swf', WindowLayer.FULLSCREEN_WINDOW, VIEW_ALIAS.LINKEDSET_HINTS, ScopeTemplates.DEFAULT_SCOPE, True),
     GroupedViewSettings(LINKEDSET_ALIASES.LINKED_SET_VEHICLE_LIST_POPUP_PY, LinkedSetVehicleListPopup, LINKEDSET_ALIASES.LINKED_SET_VEHICLE_LIST_POPUP_UI, WindowLayer.TOP_WINDOW, '', None, ScopeTemplates.DEFAULT_SCOPE, True, isModal=True))


def getBusinessHandlers():
    return (
     LinkedsetBusinessHandler(),)


class LinkedsetBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          LINKEDSET_ALIASES.LINKED_SET_DETAILS_CONTAINER_VIEW, self.loadViewByCtxEvent),
         (
          VIEW_ALIAS.LINKEDSET_HINTS, self.loadViewByCtxEvent),
         (
          LINKEDSET_ALIASES.LINKED_SET_VEHICLE_LIST_POPUP_PY, self.loadViewByCtxEvent))
        super(LinkedsetBusinessHandler, self).__init__(listeners, APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)