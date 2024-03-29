# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/epicBattleTraining/__init__.py
from frameworks.wulf import WindowLayer
from gui.Scaleform.framework import ViewSettings
from gui.Scaleform.framework import GroupedViewSettings, ScopeTemplates
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.app_loader.settings import APP_NAME_SPACE
from gui.shared import EVENT_BUS_SCOPE
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.epicBattleTraining.epic_battles_list import EpicBattlesList
    from gui.Scaleform.daapi.view.lobby.epicBattleTraining.epic_battle_training_room import EpicBattleTrainingRoom
    from gui.Scaleform.daapi.view.lobby.trainings.TrainingSettingsWindow import TrainingSettingsWindow
    return [
     ViewSettings(PREBATTLE_ALIASES.EPICBATTLE_LIST_VIEW_PY, EpicBattlesList, 'trainingForm.swf', WindowLayer.SUB_VIEW, PREBATTLE_ALIASES.EPICBATTLE_LIST_VIEW_PY, ScopeTemplates.DEFAULT_SCOPE, True),
     ViewSettings(PREBATTLE_ALIASES.EPIC_TRAINING_ROOM_VIEW_PY, EpicBattleTrainingRoom, 'EpicBattleTrainingRoom.swf', WindowLayer.SUB_VIEW, PREBATTLE_ALIASES.EPIC_TRAINING_ROOM_VIEW_PY, ScopeTemplates.DEFAULT_SCOPE, True),
     GroupedViewSettings(PREBATTLE_ALIASES.EPIC_TRAINING_SETTINGS_WINDOW_PY, TrainingSettingsWindow, 'trainingWindow.swf', WindowLayer.WINDOW, PREBATTLE_ALIASES.EPIC_TRAINING_SETTINGS_WINDOW_PY, None, ScopeTemplates.DEFAULT_SCOPE, True)]


def getBusinessHandlers():
    return (
     _EpicBattlePackageBusinessHandler(),)


class _EpicBattlePackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          PREBATTLE_ALIASES.EPICBATTLE_LIST_VIEW_PY, self.loadViewByCtxEvent),
         (
          PREBATTLE_ALIASES.EPIC_TRAINING_ROOM_VIEW_PY, self.loadViewByCtxEvent),
         (
          PREBATTLE_ALIASES.EPIC_TRAINING_SETTINGS_WINDOW_PY, self.loadViewByCtxEvent))
        super(_EpicBattlePackageBusinessHandler, self).__init__(listeners, APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)