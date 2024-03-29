# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/epicBattle/__init__.py
from frameworks.wulf import WindowLayer
from gui.Scaleform.framework import ScopeTemplates, ComponentSettings
from gui.Scaleform.framework import ViewSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.Scaleform.genConsts.EPICBATTLES_ALIASES import EPICBATTLES_ALIASES
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES
from gui.app_loader.settings import APP_NAME_SPACE
from gui.shared import EVENT_BUS_SCOPE

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.epicBattle.epic_battles_after_battle_view import EpicBattlesAfterBattleView
    from gui.Scaleform.daapi.view.lobby.epicBattle.epic_prime_time import EpicBattlesPrimeTimeView
    from gui.Scaleform.daapi.view.lobby.epicBattle.epic_quest_progress_view import EpicQuestProgressView
    return (
     ViewSettings(EPICBATTLES_ALIASES.EPIC_BATTLES_AFTER_BATTLE_ALIAS, EpicBattlesAfterBattleView, EPICBATTLES_ALIASES.EPIC_BATTLES_AFTER_BATTLE_UI, WindowLayer.TOP_WINDOW, EPICBATTLES_ALIASES.EPIC_BATTLES_AFTER_BATTLE_ALIAS, ScopeTemplates.DEFAULT_SCOPE, True),
     ViewSettings(EPICBATTLES_ALIASES.EPIC_BATTLES_PRIME_TIME_ALIAS, EpicBattlesPrimeTimeView, HANGAR_ALIASES.EPIC_PRIME_TIME, WindowLayer.SUB_VIEW, EPICBATTLES_ALIASES.EPIC_BATTLES_PRIME_TIME_ALIAS, ScopeTemplates.LOBBY_SUB_SCOPE, True),
     ComponentSettings(EPICBATTLES_ALIASES.EPIC_BATTLES_PROGRESS_INFO_ALIAS, EpicQuestProgressView, ScopeTemplates.DEFAULT_SCOPE))


def getBusinessHandlers():
    return (
     EpicMetaGamePackageBusinessHandler(),)


class EpicMetaGamePackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          EPICBATTLES_ALIASES.EPIC_BATTLES_AFTER_BATTLE_ALIAS, self.loadViewByCtxEvent),
         (
          EPICBATTLES_ALIASES.EPIC_BATTLES_PRIME_TIME_ALIAS, self.loadViewByCtxEvent))
        super(EpicMetaGamePackageBusinessHandler, self).__init__(listeners, APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)