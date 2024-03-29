# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/techtree/__init__.py
from frameworks.wulf import WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ConditionalViewSettings, ScopeTemplates, ComponentSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE
from gui.Scaleform.genConsts.RESEARCH_ALIASES import RESEARCH_ALIASES
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE, g_eventBus
from gui.Scaleform.daapi.view.bootcamp.component_override import BootcampComponentOverride

def getContextMenuHandlers():
    from gui.Scaleform.daapi.view.lobby.techtree.research_cm_handlers import ResearchVehicleContextMenuHandler, ResearchItemContextMenuHandler, BlueprintVehicleContextMenuHandler
    from gui.Scaleform.daapi.view.bootcamp.bootcamp_cm_handlers import BCResearchVehicleContextMenuHandler
    from gui.Scaleform.daapi.view.bootcamp.bootcamp_cm_handlers import BCResearchItemContextMenuHandler
    return (
     (
      CONTEXT_MENU_HANDLER_TYPE.RESEARCH_VEHICLE,
      BootcampComponentOverride(ResearchVehicleContextMenuHandler, BCResearchVehicleContextMenuHandler)),
     (
      CONTEXT_MENU_HANDLER_TYPE.RESEARCH_ITEM,
      BootcampComponentOverride(ResearchItemContextMenuHandler, BCResearchItemContextMenuHandler)),
     (
      CONTEXT_MENU_HANDLER_TYPE.BLUEPRINT_VEHICLE, BlueprintVehicleContextMenuHandler))


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.techtree.research_page import Research
    from gui.Scaleform.daapi.view.lobby.techtree.techtree_page import TechTree
    from gui.Scaleform.daapi.view.bootcamp.BCTechTree import BCTechTree
    from gui.Scaleform.daapi.view.bootcamp.BCResearch import BCResearch
    return (
     ConditionalViewSettings(VIEW_ALIAS.LOBBY_TECHTREE, BootcampComponentOverride(TechTree, BCTechTree), 'techtree.swf', WindowLayer.SUB_VIEW, None, VIEW_ALIAS.LOBBY_TECHTREE, ScopeTemplates.LOBBY_SUB_SCOPE, True),
     ConditionalViewSettings(VIEW_ALIAS.LOBBY_RESEARCH, BootcampComponentOverride(Research, BCResearch), 'research.swf', WindowLayer.SUB_VIEW, None, VIEW_ALIAS.LOBBY_RESEARCH, ScopeTemplates.LOBBY_SUB_SCOPE, True))


def getBusinessHandlers():
    return (
     _TechTreePackageBusinessHandler(),)


class _TechTreePackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          VIEW_ALIAS.LOBBY_TECHTREE, self.__loadTechTree),
         (
          VIEW_ALIAS.LOBBY_RESEARCH, self.__loadResearch),
         (
          VIEW_ALIAS.EXIT_FROM_RESEARCH, self.__exitFromResearch))
        super(_TechTreePackageBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)
        self.__exitEvent = None
        return

    def __loadTechTree(self, event):
        self.loadViewWithDefName(VIEW_ALIAS.LOBBY_TECHTREE, ctx=event.ctx)

    def __loadResearch(self, event):
        ctx = event.ctx
        self.__exitEvent = ctx.get('exit')
        self.loadViewWithDefName(VIEW_ALIAS.LOBBY_RESEARCH, ctx=ctx)

    def __exitFromResearch(self, _):
        if self.__exitEvent is not None:
            g_eventBus.handleEvent(self.__exitEvent, scope=EVENT_BUS_SCOPE.LOBBY)
        return