# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/header/__init__.py
from __future__ import absolute_import
from frameworks.wulf import WindowLayer
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import GroupedViewSettings
from gui.Scaleform.framework import ScopeTemplates, ConditionalViewSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.Scaleform.daapi.view.bootcamp.component_override import BootcampComponentOverride

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.header.BattleTypeSelectPopover import BattleTypeSelectPopover
    from gui.Scaleform.daapi.view.lobby.header.SquadTypeSelectPopover import SquadTypeSelectPopover
    from gui.Scaleform.daapi.view.lobby.header.LobbyHeader import LobbyHeader
    from gui.Scaleform.daapi.view.bootcamp.BCLobbyHeader import BCLobbyHeader
    from gui.Scaleform.daapi.view.bootcamp.BCBattleSelector import BCBattleSelector
    return (
     ConditionalViewSettings(VIEW_ALIAS.BATTLE_TYPE_SELECT_POPOVER, BootcampComponentOverride(BattleTypeSelectPopover, BCBattleSelector), 'itemSelectorPopover.swf', WindowLayer.WINDOW, VIEW_ALIAS.BATTLE_TYPE_SELECT_POPOVER, VIEW_ALIAS.BATTLE_TYPE_SELECT_POPOVER, ScopeTemplates.DEFAULT_SCOPE),
     GroupedViewSettings(VIEW_ALIAS.SQUAD_TYPE_SELECT_POPOVER, SquadTypeSelectPopover, 'itemSelectorPopover.swf', WindowLayer.WINDOW, VIEW_ALIAS.SQUAD_TYPE_SELECT_POPOVER, VIEW_ALIAS.SQUAD_TYPE_SELECT_POPOVER, ScopeTemplates.DEFAULT_SCOPE),
     ConditionalViewSettings(VIEW_ALIAS.LOBBY_HEADER, BootcampComponentOverride(LobbyHeader, BCLobbyHeader), None, WindowLayer.UNDEFINED, None, None, ScopeTemplates.DEFAULT_SCOPE))


def getBusinessHandlers():
    return (
     HeaderPackageBusinessHandler(),)


class HeaderPackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          VIEW_ALIAS.BATTLE_TYPE_SELECT_POPOVER, self.loadViewByCtxEvent),
         (
          VIEW_ALIAS.SQUAD_TYPE_SELECT_POPOVER, self.loadViewByCtxEvent))
        super(HeaderPackageBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)