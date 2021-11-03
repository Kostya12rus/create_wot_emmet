# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/ingame_menu.py
from functools import partial
import BattleReplay, constants
from account_helpers.counter_settings import getCountNewSettings
from adisp import process
from bootcamp.Bootcamp import g_bootcamp
from gui import DialogsInterface, GUI_SETTINGS
from gui import makeHtmlString
from gui.Scaleform.daapi.view.dialogs import DIALOG_BUTTON_ID
from gui.Scaleform.daapi.view.dialogs import I18nConfirmDialogMeta
from gui.Scaleform.daapi.view.dialogs.deserter_meta import IngameDeserterDialogMeta
from gui.Scaleform.daapi.view.dialogs.event_afk_dialog import EventAFKDialogMetaData
from gui.Scaleform.daapi.view.meta.IngameMenuMeta import IngameMenuMeta
from gui.Scaleform.genConsts.GLOBAL_VARS_MGR_CONSTS import GLOBAL_VARS_MGR_CONSTS
from gui.Scaleform.genConsts.INTERFACE_STATES import INTERFACE_STATES
from gui.Scaleform.locale.BOOTCAMP import BOOTCAMP
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.Scaleform.managers.battle_input import BattleGUIKeyHandler
from gui.battle_control import event_dispatcher as battle_event_dispatcher
from gui.impl.lobby.bootcamp.bootcamp_exit_view import BootcampExitWindow
from gui.shared import event_dispatcher as shared_event_dispatcher
from gui.shared import events
from gui.shared.formatters import icons
from gui.shared.utils.functions import makeTooltip
from helpers import i18n, dependency
from skeletons.connection_mgr import IConnectionManager
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.gui.game_control import IServerStatsController, IBootcampController
from skeletons.gui.lobby_context import ILobbyContext
from constants import ARENA_GUI_TYPE
_ARENAS_WITHOUT_DEZERTER_PUNISHMENTS = frozenset([ARENA_GUI_TYPE.BATTLE_ROYALE, ARENA_GUI_TYPE.EVENT_BATTLES])

class IngameMenu(IngameMenuMeta, BattleGUIKeyHandler):
    serverStats = dependency.descriptor(IServerStatsController)
    sessionProvider = dependency.descriptor(IBattleSessionProvider)
    connectionMgr = dependency.descriptor(IConnectionManager)
    bootcampController = dependency.descriptor(IBootcampController)
    lobbyContext = dependency.descriptor(ILobbyContext)

    def onWindowClose(self):
        self.destroy()

    def handleEscKey(self, isDown):
        return isDown

    def quitBattleClick(self):
        if self.app.varsManager.isTutorialRunning(GLOBAL_VARS_MGR_CONSTS.BATTLE):
            self.__doLeaveTutorial()
        else:
            self.__doLeaveArena()

    def settingsClick(self):
        shared_event_dispatcher.showSettingsWindow(redefinedKeyMode=True, isBattleSettings=True)

    def helpClick(self):
        self.destroy()
        if self.sessionProvider.arenaVisitor.gui.isEventBattle():
            battle_event_dispatcher.toggleHWIngameHelp()
        else:
            battle_event_dispatcher.toggleHelp()

    def cancelClick(self):
        self.destroy()

    def onCounterNeedUpdate(self):
        self.__updateNewSettingsCount()

    def bootcampClick(self):
        if self.bootcampController.isInBootcamp():
            self.__doLeaveBootcamp()
        else:
            self.__doLeaveArena()

    def _populate(self):
        super(IngameMenu, self)._populate()
        if self.app is not None:
            self.app.registerGuiKeyHandler(self)
        self.__setServerSettings()
        self.__setServerStats()
        self.__setMenuButtonsLabels()
        self.as_showQuitButtonS(BattleReplay.g_replayCtrl.isPlaying or not self.bootcampController.isInBootcamp())
        isInBootcamp = self.bootcampController.isInBootcamp()
        self.as_showBootcampButtonS(isInBootcamp)
        self.as_showHelpButtonS(not isInBootcamp)
        return

    def __updateNewSettingsCount(self):
        newSettingsCount = getCountNewSettings()
        if newSettingsCount > 0:
            self.as_setCounterS([{'componentId': 'settingsBtn', 'count': str(newSettingsCount)}])
        else:
            self.as_removeCounterS(['settingsBtn'])

    def _dispose(self):
        if self.app is not None:
            self.app.unregisterGuiKeyHandler(self)
        super(IngameMenu, self)._dispose()
        return

    def __setServerSettings(self):
        if BattleReplay.g_replayCtrl.isPlaying or self.bootcampController.isInBootcamp():
            serverName = ''
            tooltipFullData = ''
            state = INTERFACE_STATES.HIDE_ALL_SERVER_INFO
        else:
            tooltipBody = i18n.makeString(TOOLTIPS.HEADER_INFO_PLAYERS_ONLINE_FULL_BODY)
            tooltipFullData = makeTooltip(TOOLTIPS.HEADER_INFO_PLAYERS_ONLINE_FULL_HEADER, tooltipBody % {'servername': self.connectionMgr.serverUserName})
            serverName = makeHtmlString('html_templates:lobby/serverStats', 'serverName', {'name': self.connectionMgr.serverUserName})
            if constants.IS_SHOW_SERVER_STATS:
                state = INTERFACE_STATES.SHOW_ALL
            else:
                state = INTERFACE_STATES.HIDE_SERVER_STATS
        self.as_setServerSettingS(serverName, tooltipFullData, state)

    def __setServerStats(self):
        if constants.IS_SHOW_SERVER_STATS and not self.bootcampController.isInBootcamp():
            self.as_setServerStatsS(*self.serverStats.getFormattedStats())

    def __setMenuButtonsLabels(self):
        bootcampIcon = RES_ICONS.MAPS_ICONS_BOOTCAMP_MENU_MENUBOOTCAMPICON
        bootcampIconSource = icons.makeImageTag(bootcampIcon, 33, 27, -8, 0)
        if self.app.varsManager.isTutorialRunning(GLOBAL_VARS_MGR_CONSTS.BATTLE):
            quitLabel = MENU.LOBBY_MENU_BUTTONS_REFUSE_TRAINING
        elif BattleReplay.isPlaying():
            quitLabel = MENU.INGAME_MENU_BUTTONS_REPLAYEXIT
        else:
            quitLabel = MENU.INGAME_MENU_BUTTONS_LOGOFF
        if self.bootcampController.isInBootcamp():
            bootcampLabel = BOOTCAMP.REQUEST_BOOTCAMP_FINISH
        elif self.bootcampController.runCount() > 0:
            bootcampLabel = BOOTCAMP.REQUEST_BOOTCAMP_RETURN
        else:
            bootcampLabel = BOOTCAMP.REQUEST_BOOTCAMP_START
        self.as_setMenuButtonsLabelsS(MENU.INGAME_MENU_BUTTONS_HELP, MENU.INGAME_MENU_BUTTONS_SETTINGS, MENU.INGAME_MENU_BUTTONS_BACK, quitLabel, bootcampLabel, bootcampIconSource)

    @process
    def __doLeaveTutorial(self):
        result = yield DialogsInterface.showDialog(I18nConfirmDialogMeta('refuseTraining', focusedID=DIALOG_BUTTON_ID.CLOSE))
        if result:
            self.fireEvent(events.TutorialEvent(events.TutorialEvent.STOP_TRAINING))
            self.destroy()

    @process
    def __doLeaveArena(self):
        exitResult = self.sessionProvider.getExitResult()
        arenaType = self.sessionProvider.arenaVisitor.getArenaGuiType()
        if not BattleReplay.isPlaying() and self._isEventPrematureLeave():
            result = yield DialogsInterface.showDialog(EventAFKDialogMetaData(EventAFKDialogMetaData.BATTLE_WARNING))
        elif exitResult.isDeserter and arenaType not in _ARENAS_WITHOUT_DEZERTER_PUNISHMENTS:
            quitBattleKey = self.__getQuitBattleKey(exitResult.playerInfo)
            result = yield DialogsInterface.showDialog(IngameDeserterDialogMeta(quitBattleKey + '/deserter', focusedID=DIALOG_BUTTON_ID.CLOSE))
        elif BattleReplay.isPlaying():
            result = yield DialogsInterface.showDialog(I18nConfirmDialogMeta('quitReplay', focusedID=DIALOG_BUTTON_ID.CLOSE))
        else:
            result = yield DialogsInterface.showDialog(I18nConfirmDialogMeta('quitBattle', focusedID=DIALOG_BUTTON_ID.CLOSE))
        if result:
            self.__doExit()

    def __doExit(self):
        self.sessionProvider.exit()
        self.destroy()

    @staticmethod
    def __getQuitBattleKey(playerInfo):
        igrType = playerInfo.igrType if playerInfo else constants.IGR_TYPE.NONE
        if constants.IS_KOREA and GUI_SETTINGS.igrEnabled and igrType != constants.IGR_TYPE.NONE:
            return 'quitBattleIGR'
        return 'quitBattle'

    def showBootcampExitWindow(self):
        window = BootcampExitWindow(partial(self.bootcampController.stopBootcamp, True), True)
        window.load()

    @process
    def __doLeaveBootcamp(self):
        if g_bootcamp.getLessonNum() == g_bootcamp.getContextIntParameter('lastLessonNum') - 1:
            exitResult = self.sessionProvider.getExitResult()
            quitBattleKey = self.__getQuitBattleKey(exitResult.playerInfo)
            result = yield DialogsInterface.showDialog(IngameDeserterDialogMeta(quitBattleKey + '/deserter', focusedID=DIALOG_BUTTON_ID.CLOSE))
            if result:
                self.showBootcampExitWindow()
        else:
            self.showBootcampExitWindow()
        self.destroy()

    def _getGameEventComponent(self):
        componentSystem = self.sessionProvider.arenaVisitor.getComponentSystem()
        if componentSystem is None:
            return
        else:
            return getattr(componentSystem, 'gameEventComponent', None)

    def _getEnvironmentData(self):
        gameEventStorage = self._getGameEventComponent()
        if gameEventStorage is None:
            return
        else:
            return gameEventStorage.getEnvironmentData()

    def _isEventPrematureLeave(self):
        if not self.sessionProvider.arenaVisitor.gui.isEventBattle():
            return False
        else:
            envData = self._getEnvironmentData()
            if envData is None:
                return False
            inPostmortem = self.sessionProvider.shared.vehicleState.isInPostmortem
            if envData.getCurrentEnvironmentID() >= envData.getMaxEnvironmentID() and inPostmortem:
                return False
            return True