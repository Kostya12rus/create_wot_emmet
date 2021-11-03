# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_control/maps_training_controller.py
import typing
from functools import partial
import ArenaType, adisp
from BattleReplay import g_replayCtrl, CallbackDataNames
import BigWorld, Event
from CurrentVehicle import g_currentPreviewVehicle
from PlayerEvents import g_playerEvents
from constants import ARENA_BONUS_TYPE, REQUEST_COOLDOWN
from gui.impl.lobby.maps_training.maps_training_client_settings import MapsTrainingClientSettings
from gui.prb_control.entities.base.ctx import PrbAction
from helpers import dependency
from helpers import isPlayerAccount
from items.vehicles import getVehicleClass
from maps_training_common.helpers import unpackMapsTrainingScenarios, unpackMapsTrainingRewards
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.gui.lobby_context import ILobbyContext
from wotdecorators import condition
from AccountCommands import isCodeValid
from debug_utils import LOG_ERROR
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.prb_control.entities.listener import IGlobalListener
from gui.prb_control.settings import FUNCTIONAL_FLAG, PREBATTLE_ACTION_NAME
from gui.shared import events, EVENT_BUS_SCOPE, g_eventBus
from items import vehicles
from gui.shared import event_dispatcher
from skeletons.gui.game_control import IMapsTrainingController

class MapsTrainingController(IMapsTrainingController, IGlobalListener):
    lobbyContext = dependency.descriptor(ILobbyContext)
    sessionProvider = dependency.descriptor(IBattleSessionProvider)
    ifEnabled = condition('isMapsTrainingEnabled')
    ifMapsTrainingPrbActive = condition('isMapsTrainingPrbActive')
    _UNDEFINED_VALUE = -1

    def __init__(self):
        self.__config = {}
        self.__mapGeometryID = self._UNDEFINED_VALUE
        self.__vehCompDescr = self._UNDEFINED_VALUE
        self.__team = 1
        self.__replayCallbacks = []
        self.__replayConfigStored = False
        self.__preferences = MapsTrainingClientSettings()
        self.__configIsOld = False
        self.__lastRequestTime = 0
        self.onUpdated = Event.Event()

    @property
    def isMapsTrainingEnabled(self):
        return self.lobbyContext.getServerSettings().isMapsTrainingEnabled()

    @property
    def isMapsTrainingPrbActive(self):
        if self.prbEntity is None:
            return False
        else:
            return bool(self.prbEntity.getModeFlags() & FUNCTIONAL_FLAG.MAPS_TRAINING)

    @property
    def preferences(self):
        return self.__preferences

    @ifEnabled
    @ifMapsTrainingPrbActive
    def showMapsTrainingPage(self, ctx=None):
        if ctx is None:
            ctx = self.getPageCtx()
        event_dispatcher.showMapsTrainingPage(ctx)
        return

    @ifEnabled
    @ifMapsTrainingPrbActive
    def showMapsTrainingQueue(self):
        event_dispatcher.showMapsTrainingQueue()

    @adisp.process
    def selectMapsTrainingMode(self):
        dispatcher = self.prbDispatcher
        if dispatcher is None:
            return
        else:
            isSuccess = yield dispatcher.doSelectAction(PrbAction(PREBATTLE_ACTION_NAME.MAPS_TRAINING))
            if isSuccess:
                self.showMapsTrainingPage()
            return

    @adisp.process
    def selectRandomMode(self):
        dispatcher = self.prbDispatcher
        if dispatcher is None:
            return
        else:
            yield dispatcher.doSelectAction(PrbAction(PREBATTLE_ACTION_NAME.RANDOM))
            return

    def getSelectedMap(self):
        return self.__mapGeometryID

    def setSelectedMap(self, mapName):
        self.__mapGeometryID = self._UNDEFINED_VALUE
        if mapName:
            self.__mapGeometryID = ArenaType.g_geometryNamesToIDs[mapName]
        self.onUpdated()

    def getSelectedVehicle(self):
        return self.__vehCompDescr

    def setSelectedVehicle(self, vehicleName):
        if vehicleName:
            nationID, vehID = vehicles.g_list.getIDsByName(vehicleName)
            self.__vehCompDescr = vehicles.makeIntCompactDescrByID('vehicle', nationID, vehID)
            g_currentPreviewVehicle.selectVehicle(self.__vehCompDescr)
        else:
            self.__vehCompDescr = self._UNDEFINED_VALUE
            g_currentPreviewVehicle.selectNoVehicle()
        self.onUpdated()

    def getSelectedTeam(self):
        return self.__team

    def setSelectedTeam(self, team):
        self.__team = team

    def isValid(self):
        return self.isMapsTrainingEnabled and self.isMapsTrainingPrbActive and self.__mapGeometryID > 0 and self.__vehCompDescr > 0

    def reset(self):
        self.__mapGeometryID = self._UNDEFINED_VALUE
        self.__vehCompDescr = self._UNDEFINED_VALUE
        self.__team = 1
        g_currentPreviewVehicle.selectNoVehicle()

    def init(self):
        super(MapsTrainingController, self).init()
        g_replayCtrl.setDataCallback(CallbackDataNames.MT_CONFIG_CALLBACK, self.__restoreConfigFromReplay)

    def fini(self):
        g_replayCtrl.delDataCallback(CallbackDataNames.MT_CONFIG_CALLBACK, self.__restoreConfigFromReplay)
        self.lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingChanged
        super(MapsTrainingController, self).fini()

    def onEnter(self):
        self.__preferences.load()
        g_playerEvents.onDisconnected += self.__onDisconnected
        g_eventBus.addListener(events.ViewEventType.LOAD_VIEW, self.__viewLoaded, EVENT_BUS_SCOPE.LOBBY)
        self.lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingChanged
        if self.__isAfterBattle():
            battleCtx = self.sessionProvider.getCtx()
            event_dispatcher.showMapsTrainingResultsWindow(battleCtx.lastArenaUniqueID, False)
        else:
            self.showMapsTrainingPage()

    def onExit(self):
        self.reset()
        self.__preferences.resetSessionFilters()
        g_currentPreviewVehicle.resetAppearance()
        g_playerEvents.onDisconnected -= self.__onDisconnected
        g_eventBus.removeListener(events.ViewEventType.LOAD_VIEW, self.__viewLoaded, EVENT_BUS_SCOPE.LOBBY)

    def getConfig(self):
        return self.__config

    def onAccountBecomeNonPlayer(self):
        self.__replayConfigStored = False

    def requestInitialDataFromServer(self, callback=None):
        if g_replayCtrl.isRecording and not self.__replayConfigStored:
            g_replayCtrl.serializeCallbackData(CallbackDataNames.MT_CONFIG_CALLBACK, (self.__config,))
            self.__replayConfigStored = True
        if self.__config and not self.__configIsOld and callback:
            return callback()
        if g_replayCtrl.isPlaying:
            self.__replayCallbacks.append(callback)
        else:
            self.__lastRequestTime = BigWorld.time()
            account = BigWorld.player()
            account.requestMapsTrainingInitialConfiguration(account.databaseID, partial(self.__processConfiguration, callback))
        self.__configIsOld = False

    def getPageCtx(self):
        return {'map': ArenaType.g_geometryCache[self.__mapGeometryID].geometryName if self.__mapGeometryID != self._UNDEFINED_VALUE else '', 
           'vehicleType': getVehicleClass(self.__vehCompDescr) if self.__vehCompDescr != self._UNDEFINED_VALUE else '', 
           'side': self.__team}

    def __isAfterBattle(self):
        battleCtx = self.sessionProvider.getCtx()
        return bool(battleCtx.lastArenaUniqueID) and battleCtx.lastArenaBonusType == ARENA_BONUS_TYPE.MAPS_TRAINING

    @ifEnabled
    @ifMapsTrainingPrbActive
    def __viewLoaded(self, event):
        if event.alias == VIEW_ALIAS.LOBBY_HANGAR and not self.__isAfterBattle():
            self.showMapsTrainingPage()

    def __processConfiguration(self, callback, code, errStr, value):
        if not isCodeValid(code):
            LOG_ERROR(errStr)
            return
        self.__parseConfiguration(value)
        if callback:
            callback()

    def __parseConfiguration(self, configuration):
        configMaps = {}
        configVehicles = {}
        confScenarios = {}
        configRewards = {}
        for mapGeometryID, difficulty, availableVehicles, availableScenarios, availableRewards in configuration:
            configMaps[mapGeometryID] = difficulty
            configVehicles[mapGeometryID] = []
            for team in availableVehicles:
                for vehCD in team[1]:
                    if vehCD not in configVehicles[mapGeometryID]:
                        configVehicles[mapGeometryID].append(vehCD)

            confScenarios[mapGeometryID] = unpackMapsTrainingScenarios(availableScenarios)
            configRewards[mapGeometryID] = unpackMapsTrainingRewards(availableRewards)

        self.__config.update({'maps': configMaps, 
           'vehicles': configVehicles, 
           'scenarios': confScenarios, 
           'rewards': configRewards})

    def __restoreConfigFromReplay(self, config):
        if g_replayCtrl.isPlaying:
            self.__config = config
            for cb in self.__replayCallbacks:
                self.requestInitialDataFromServer(cb)

            self.__replayCallbacks = []

    def __onServerSettingChanged(self, diff):
        self.__configIsOld = True
        if isPlayerAccount():
            cooldownDelta = BigWorld.time() - self.__lastRequestTime
            if not self.__lastRequestTime or cooldownDelta < REQUEST_COOLDOWN.MAPS_TRAINING_INITIAL_CONFIGURATION:
                self.requestInitialDataFromServer()
            else:
                self.__configIsOld = False
        if not diff.get('isMapsTrainingEnabled', True):
            if self.isMapsTrainingPrbActive and not self.prbEntity.isInQueue():
                self.selectRandomMode()

    def __onDisconnected(self):
        self.__preferences.resetSessionFilters()
        self.reset()