# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/crewOperations/__init__.py
from frameworks.wulf import WindowLayer
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import GroupedViewSettings, ScopeTemplates
from gui.Scaleform.framework.package_layout import PackageBusinessHandler

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.crewOperations.CrewOperationsPopOver import CrewOperationsPopOver
    from gui.Scaleform.daapi.view.lobby.crewOperations.RetrainCrewWindow import RetrainCrewWindow
    return (
     GroupedViewSettings(VIEW_ALIAS.CREW_OPERATIONS_POPOVER, CrewOperationsPopOver, 'crewOperationsPopOver.swf', WindowLayer.WINDOW, 'crewOperationsPopOver', VIEW_ALIAS.CREW_OPERATIONS_POPOVER, ScopeTemplates.WINDOW_VIEWED_MULTISCOPE),
     GroupedViewSettings(VIEW_ALIAS.RETRAIN_CREW, RetrainCrewWindow, 'retrainCrewWindow.swf', WindowLayer.TOP_WINDOW, 'retrainCrewWindow', None, ScopeTemplates.DEFAULT_SCOPE, isModal=True, canDrag=False))


def getBusinessHandlers():
    return (
     CrewOpsBusinessHandler(),)


class CrewOpsBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          VIEW_ALIAS.CREW_OPERATIONS_POPOVER, self.loadViewByCtxEvent),
         (
          VIEW_ALIAS.RETRAIN_CREW, self.loadViewByCtxEvent))
        super(CrewOpsBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)