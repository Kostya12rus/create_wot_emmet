# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/lobby_context.py
from helpers.server_settings import ServerSettings
import BigWorld
from Event import Event, EventManager
from account_helpers import isRoamingEnabled
from adisp import adisp_async, adisp_process
from constants import CURRENT_REALM, Configs
from debug_utils import LOG_ERROR, LOG_NOTE
from gui.lobby_ctx_listener import LobbyContextChangeListener
from helpers import dependency
from ids_generators import Int32IDGenerator
from predefined_hosts import g_preDefinedHosts
from skeletons.connection_mgr import IConnectionManager
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache

class LobbyContext(ILobbyContext):
    connectionMgr = dependency.descriptor(IConnectionManager)

    def __init__(self):
        super(LobbyContext, self).__init__()
        self.__credentials = None
        self.__guiCtx = {}
        self.__arenaUniqueIDs = {}
        self.__serverSettings = ServerSettings({})
        self.__battlesCount = None
        self.__epicBattlesCount = None
        self.__clientArenaIDGenerator = Int32IDGenerator()
        self.__headerNavigationConfirmators = set()
        self.__fightButtonConfirmators = set()
        self.__platoonCreationConfirmators = set()
        self.__changeListener = LobbyContextChangeListener(self)
        self.__isAccountComplete = True
        self.__em = EventManager()
        self.onServerSettingsChanged = Event(self.__em)
        return

    @property
    def collectUiStats(self):
        return self.__guiCtx.get('collectUiStats', True)

    @property
    def needLogUXEvents(self):
        return self.__guiCtx.get('logUXEvents', False)

    def clear(self):
        self.__headerNavigationConfirmators.clear()
        self.__fightButtonConfirmators.clear()
        self.__platoonCreationConfirmators.clear()
        self.__credentials = None
        self.__battlesCount = None
        self.__guiCtx.clear()
        self.__arenaUniqueIDs.clear()
        if self.__serverSettings:
            self.__serverSettings.clear()
        self.__em.clear()
        return

    def onAccountBecomePlayer(self):
        self.setServerSettings(BigWorld.player().serverSettings)

    def onAccountShowGUI(self, ctx):
        self.__guiCtx = ctx or {}

    def getArenaUniqueIDByClientID(self, clientArenaID):
        for arenaUniqueID, cArenaID in self.__arenaUniqueIDs.iteritems():
            if cArenaID == clientArenaID:
                return arenaUniqueID

        return 0

    def getClientIDByArenaUniqueID(self, arenaUniqueID):
        if arenaUniqueID in self.__arenaUniqueIDs:
            return self.__arenaUniqueIDs[arenaUniqueID]
        clientID = self.__clientArenaIDGenerator.next()
        self.__arenaUniqueIDs[arenaUniqueID] = clientID
        return clientID

    def setCredentials(self, login, token):
        self.__credentials = (
         login, token)

    def getCredentials(self):
        return self.__credentials

    def isAccountComplete(self):
        return self.__isAccountComplete

    def setAccountComplete(self, isComplete):
        self.__isAccountComplete = isComplete

    def getBattlesCount(self):
        return self.__battlesCount

    def getEpicBattlesCount(self):
        return self.__epicBattlesCount

    def updateBattlesCount(self, battlesCount, epicBattlesCount):
        self.__battlesCount = battlesCount
        self.__epicBattlesCount = epicBattlesCount

    def update(self, diff):
        if self.__serverSettings:
            if 'serverSettings' in diff:
                self.__notifyToUpdate(diff['serverSettings'])
                self.__changeListener.update(diff['serverSettings'])
                self.__serverSettings.update(diff['serverSettings'])
            elif ('serverSettings', '_r') in diff:
                self.__notifyToUpdate(diff[('serverSettings', '_r')])
                self.__changeListener.update(diff[('serverSettings', '_r')])
                self.__serverSettings.set(diff[('serverSettings', '_r')])

    def updateGuiCtx(self, ctx):
        self.__guiCtx.update(ctx)

    def getGuiCtx(self):
        return self.__guiCtx

    def getServerSettings(self):
        return self.__serverSettings

    def setServerSettings(self, serverSettings):
        if self.__serverSettings:
            self.__serverSettings.clear()
        self.__serverSettings = ServerSettings(serverSettings)
        self.onServerSettingsChanged(self.__serverSettings)

    def getPlayerFullName(self, pName, clanInfo=None, clanAbbrev=None, regionCode=None, pDBID=None):
        fullName = pName
        if clanInfo and len(clanInfo) > 1:
            clanAbbrev = clanInfo[1]
        if clanAbbrev:
            fullName = ('{0:>s} [{1:>s}]').format(pName, clanAbbrev)
        if pDBID is not None:
            regionCode = self.getRegionCode(pDBID)
        if regionCode:
            fullName = ('{0:>s} {1:>s}').format(fullName, regionCode)
        return fullName

    def getClanAbbrev(self, clanInfo):
        clanAbbrev = None
        if clanInfo and len(clanInfo) > 1:
            clanAbbrev = clanInfo[1]
        return clanAbbrev

    def getRegionCode(self, dbID):
        regionCode = None
        serverSettings = self.getServerSettings()
        if serverSettings is not None:
            roaming = serverSettings.roaming
            if dbID and not roaming.isSameRealm(dbID):
                _, regionCode = roaming.getPlayerHome(dbID)
        return regionCode

    def isAnotherPeriphery(self, peripheryID):
        if not self._isSkipPeripheryChecking():
            return self.connectionMgr.peripheryID != peripheryID
        LOG_NOTE('Skip periphery checking in standalone mode')
        return False

    @dependency.replace_none_kwargs(itemsCache=IItemsCache)
    def isPeripheryAvailable(self, peripheryID, itemsCache=None):
        result = True
        if self._isSkipPeripheryChecking():
            LOG_NOTE('Skip periphery checking in standalone mode')
            return result
        else:
            if g_preDefinedHosts.periphery(peripheryID) is None:
                LOG_ERROR('Periphery not found', peripheryID)
                result = False
            elif self.__credentials is None:
                LOG_ERROR('Login info not found', peripheryID)
                result = False
            elif g_preDefinedHosts.isRoamingPeriphery(peripheryID) and itemsCache is not None and not isRoamingEnabled(itemsCache.items.stats.attributes):
                LOG_ERROR('Roaming is not supported', peripheryID)
                result = False
            return result

    def getPeripheryName(self, peripheryID, checkAnother=True, useShortName=False):
        name = None
        if not checkAnother or self.isAnotherPeriphery(peripheryID):
            host = g_preDefinedHosts.periphery(peripheryID)
            if host is not None:
                name = host.shortName if useShortName else host.name
        return name

    def addHeaderNavigationConfirmator(self, confirmator):
        self.__headerNavigationConfirmators.add(confirmator)

    def deleteHeaderNavigationConfirmator(self, confirmator):
        if confirmator in self.__headerNavigationConfirmators:
            self.__headerNavigationConfirmators.remove(confirmator)

    @adisp_async
    @adisp_process
    def isHeaderNavigationPossible(self, callback=None):
        for confirmator in set(self.__headerNavigationConfirmators):
            confirmed = yield confirmator()
            if not confirmed:
                callback(False)

        callback(True)

    def addFightButtonConfirmator(self, confirmator):
        self.__fightButtonConfirmators.add(confirmator)

    def deleteFightButtonConfirmator(self, confirmator):
        if confirmator in self.__fightButtonConfirmators:
            self.__fightButtonConfirmators.remove(confirmator)

    @adisp_async
    @adisp_process
    def isFightButtonPressPossible(self, callback=None):
        for confirmator in self.__fightButtonConfirmators:
            confirmed = yield confirmator()
            if not confirmed:
                callback(False)

        callback(True)

    def addPlatoonCreationConfirmator(self, confirmator):
        self.__platoonCreationConfirmators.add(confirmator)

    def deletePlatoonCreationConfirmator(self, confirmator):
        if confirmator in self.__platoonCreationConfirmators:
            self.__platoonCreationConfirmators.remove(confirmator)

    @adisp_async
    @adisp_process
    def isPlatoonCreationPossible(self, callback=None):
        for confirmator in self.__platoonCreationConfirmators:
            confirmed = yield confirmator()
            if not confirmed:
                callback(False)

        callback(True)

    @classmethod
    def _isSkipPeripheryChecking(cls):
        return cls.connectionMgr.isStandalone() and CURRENT_REALM == 'CT'

    @dependency.replace_none_kwargs(itemsCache=IItemsCache)
    def __notifyToUpdate(self, diff, itemsCache=None):
        if 'lootBoxes_config' in diff:
            itemsCache.items.tokens.updateAllLootBoxes(diff['lootBoxes_config'])
        if Configs.RESTORE_CONFIG.value in diff:
            itemsCache.items.invalidateCache({Configs.RESTORE_CONFIG.value: diff[Configs.RESTORE_CONFIG.value]})