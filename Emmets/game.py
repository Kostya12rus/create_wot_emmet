# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/game.py
import cPickle, functools, locale, sys, zlib, Account, AreaDestructibles, BigWorld, CommandMapping, GUI, MusicControllerWWISE, Settings, SoundGroups, TriggersManager, VOIP, WebBrowser, constants, services_config
from MemoryCriticalController import g_critMemHandler
from bootcamp.Bootcamp import g_bootcamp
from debug_utils import LOG_CURRENT_EXCEPTION, LOG_DEBUG, LOG_ERROR, LOG_NOTE
from gui import CLIENT_ENCODING, onRepeatKeyEvent, g_keyEventHandlers, g_mouseEventHandlers, InputHandler
from gui.Scaleform.game_loading import GameLoading
from gui.shared import personality as gui_personality
from helpers import RSSDownloader, OfflineMode, LightingGenerationMode
from helpers import dependency, log
from messenger import MessengerEntry
from skeletons.connection_mgr import IConnectionManager
from skeletons.gameplay import IGameplayLogic
from wg_async import wg_async, wg_await
from gui.impl.dialogs import dialogs
from system_events import g_systemEvents
loadingScreenClass = GameLoading
__import__('__main__').GameLoading = loadingScreenClass
try:
    locale.setlocale(locale.LC_TIME, '')
except locale.Error:
    LOG_CURRENT_EXCEPTION()

class ServiceLocator(object):
    connectionMgr = dependency.descriptor(IConnectionManager)
    gameplay = dependency.descriptor(IGameplayLogic)


g_replayCtrl = None

def autoFlushPythonLog():
    BigWorld.flushPythonLog()
    BigWorld.callback(5.0, autoFlushPythonLog)


def init(scriptConfig, engineConfig, userPreferences, loadingScreenGUI=None):
    global g_replayCtrl
    try:
        log.config.setupFromXML()
        import extension_rules
        extension_rules.init()
        import python_macroses
        python_macroses.init()
        import arena_bonus_type_caps
        arena_bonus_type_caps.init()
        if constants.IS_DEVELOPMENT:
            autoFlushPythonLog()
            from development_features import initDevBonusTypes
            initDevBonusTypes()
        BigWorld.wg_initCustomSettings()
        Settings.g_instance = Settings.Settings(scriptConfig, engineConfig, userPreferences)
        CommandMapping.g_instance = CommandMapping.CommandMapping()
        from helpers import DecalMap
        DecalMap.g_instance = DecalMap.DecalMap(scriptConfig['decal'])
        from helpers import EdgeDetectColorController
        EdgeDetectColorController.g_instance = EdgeDetectColorController.EdgeDetectColorController(scriptConfig['silhouetteColors'])
        SoundGroups.g_instance = SoundGroups.SoundGroups()
        import BattleReplay
        g_replayCtrl = BattleReplay.g_replayCtrl = BattleReplay.BattleReplay()
        g_replayCtrl.registerWotReplayFileExtension()
        g_bootcamp.replayCallbackSubscribe()
        import nation_change
        nation_change.init()
        import items
        items.init(True, None if not constants.IS_DEVELOPMENT else {})
        import battle_results
        battle_results.init()
        import win_points
        win_points.init()
        import rage
        rage.init()
        import ArenaType
        ArenaType.init()
        import dossiers2
        dossiers2.init()
        import personal_missions
        personal_missions.init()
        import motivation_quests
        motivation_quests.init()
        import customization_quests
        customization_quests.init()
        BigWorld.worldDrawEnabled(False)
        manager = dependency.configure(services_config.getClientServicesConfig)
        g_systemEvents.onDependencyConfigReady(manager)
        SoundGroups.g_instance.startListeningGUISpaceChanges()
        gui_personality.init(loadingScreenGUI=loadingScreenGUI)
        EdgeDetectColorController.g_instance.create()
        g_replayCtrl.subscribe()
        MessengerEntry.g_instance.init()
        AreaDestructibles.init()
        MusicControllerWWISE.create()
        TriggersManager.init()
        RSSDownloader.init()
        items.clearXMLCache()
        import player_ranks
        player_ranks.init()
        import destructible_entities
        destructible_entities.init()
        from AvatarInputHandler.cameras import FovExtended
        FovExtended.instance().resetFov()
        BigWorld.pauseDRRAutoscaling(True)
        if constants.HAS_DEV_RESOURCES:
            import development
            development.init()
    except Exception:
        LOG_CURRENT_EXCEPTION()
        BigWorld.quit()

    return


def start():
    LOG_DEBUG('start')
    checkBotNet()
    if OfflineMode.onStartup():
        LOG_DEBUG('OfflineMode')
        return
    else:
        if LightingGenerationMode.onStartup():
            LOG_DEBUG('LightingGenerationMode')
            return
        ServiceLocator.connectionMgr.onConnected += onConnected
        ServiceLocator.connectionMgr.onDisconnected += onDisconnected
        if len(sys.argv) > 2:
            if sys.argv[1] == 'scriptedTest':
                try:
                    scriptName = sys.argv[2]
                    if scriptName[-3:] == '.py':
                        scriptName = scriptName[:-3]
                    try:
                        __import__(scriptName)
                    except ImportError:
                        try:
                            __import__('tests.' + scriptName)
                        except ImportError:
                            __import__('Cat.' + scriptName)

                    ServiceLocator.gameplay.start()
                except Exception:
                    LOG_CURRENT_EXCEPTION()
                    BigWorld.wg_writeToStdOut('Failed to run scripted test, Python exception was thrown, see python.log')
                    BigWorld.quit()

            elif sys.argv[1] == 'offlineTest':
                try:
                    from Cat.Tasks.TestArena2 import TestArena2Object
                    LOG_DEBUG(sys.argv)
                    LOG_DEBUG('starting offline test: %s', sys.argv[2])
                    if len(sys.argv) > 3:
                        TestArena2Object.startOffline(sys.argv[2], sys.argv[3])
                    else:
                        TestArena2Object.startOffline(sys.argv[2])
                except Exception:
                    LOG_DEBUG('Game start FAILED with:')
                    LOG_CURRENT_EXCEPTION()

            else:
                if sys.argv[1] == 'hangarOverride':
                    try:
                        LOG_DEBUG(sys.argv)
                        from Tests.auto.HangarOverride import HangarOverride
                        HangarOverride.setHangar('spaces/' + sys.argv[2])
                        if len(sys.argv) > 3 and sys.argv[3] is not None:
                            LOG_DEBUG('Setting default client inactivity timeout: %s' % sys.argv[3])
                            constants.CLIENT_INACTIVITY_TIMEOUT = int(sys.argv[3])
                    except Exception:
                        LOG_DEBUG('Game start FAILED with:')
                        LOG_CURRENT_EXCEPTION()

                    ServiceLocator.gameplay.start()
                else:
                    ServiceLocator.gameplay.start()
        else:
            ServiceLocator.gameplay.start()
        BigWorld.loginEntered()
        if not g_replayCtrl.isPlaying:
            WebBrowser.initExternalCache()
        return


def abort():
    BigWorld.callback(0.0, fini)


def fini():
    global g_replayCtrl
    LOG_DEBUG('fini')
    if g_replayCtrl is not None:
        g_replayCtrl.stop(isDestroyed=True)
    BigWorld.wg_setScreenshotNotifyCallback(None)
    g_critMemHandler.restore()
    g_critMemHandler.destroy()
    if constants.IS_CAT_LOADED:
        import Cat
        Cat.fini()
    MusicControllerWWISE.destroy()
    if RSSDownloader.g_downloader is not None:
        RSSDownloader.g_downloader.destroy()
    ServiceLocator.connectionMgr.onConnected -= onConnected
    ServiceLocator.connectionMgr.onDisconnected -= onDisconnected
    MessengerEntry.g_instance.fini()
    from helpers import EdgeDetectColorController
    if EdgeDetectColorController.g_instance is not None:
        EdgeDetectColorController.g_instance.destroy()
        EdgeDetectColorController.g_instance = None
    BigWorld.resetEntityManager(False, False)
    BigWorld.clearAllSpaces()
    if TriggersManager.g_manager is not None:
        TriggersManager.g_manager.destroy()
        TriggersManager.g_manager = None
    if g_replayCtrl is not None:
        g_replayCtrl.unsubscribe()
    gui_personality.fini()
    from predefined_hosts import g_preDefinedHosts
    if g_preDefinedHosts is not None:
        g_preDefinedHosts.fini()
    SoundGroups.g_instance.stopListeningGUISpaceChanges()
    dependency.clear()
    if g_replayCtrl is not None:
        g_replayCtrl.destroy()
        g_replayCtrl = None
    voipRespHandler = VOIP.getVOIPManager()
    if voipRespHandler is not None:
        voipRespHandler.destroy()
    SoundGroups.g_instance.destroy()
    Settings.g_instance.save()
    WebBrowser.destroyExternalCache()
    if constants.HAS_DEV_RESOURCES:
        import development
        development.fini()
    return


def onChangeEnvironments(inside):
    pass


def onBeforeSend():
    g_systemEvents.onBeforeSend()


def onRecreateDevice():
    gui_personality.onRecreateDevice()


def onStreamComplete(streamID, desc, data):
    try:
        origPacketLen, origCrc32 = cPickle.loads(desc)
    except Exception:
        origPacketLen, origCrc32 = (-1, -1)

    packetLen = len(data)
    crc32 = zlib.crc32(data)
    isCorrupted = origPacketLen != packetLen or origCrc32 != crc32
    desc = (isCorrupted, origPacketLen, packetLen, origCrc32, crc32)
    player = BigWorld.player()
    if player is None:
        LOG_ERROR('onStreamComplete: no player entity available for process stream (%d, %s) data' % (streamID, desc))
    else:
        player.onStreamComplete(streamID, desc, data)
    return


def onConnected():
    gui_personality.onConnected()
    VOIP.getVOIPManager().onConnected()


def onGeometryMapped(spaceID, path):
    SoundGroups.g_instance.unloadAll()
    LOG_NOTE('[SPACE] Loading space: ' + path)
    arenaName = path.split('/')[-1]
    BigWorld.notifySpaceChange(path)
    SoundGroups.g_instance.preloadSoundGroups(arenaName)
    from ArenaType import g_geometryNamesToIDs
    if arenaName not in g_geometryNamesToIDs:
        return None
    else:
        return g_geometryNamesToIDs[arenaName]


def onDisconnected():
    BigWorld.loginEntered()
    gui_personality.onDisconnected()
    VOIP.getVOIPManager().logout()
    VOIP.getVOIPManager().onDisconnected()


def onFini():
    Account.delAccountRepository()


def onCameraChange(oldCamera):
    pass


def handleCharEvent(char, key, mods):
    char = unicode(char.encode('iso8859'), CLIENT_ENCODING)
    if GUI.handleCharEvent(char, key, mods):
        return True
    return False


def handleAxisEvent(event):
    return False


def handleKeyEvent(event):
    if constants.HAS_DEV_RESOURCES:
        from development.dev_input_handler import g_devInputHandlerInstance
        g_devInputHandlerInstance.handleKeyEvent(event)
    if OfflineMode.handleKeyEvent(event):
        return True
    else:
        if LightingGenerationMode.handleKeyEvent(event):
            return True
        isDown, key, mods, isRepeat = convertKeyEvent(event)
        if g_bootcamp.isRunning():
            g_bootcamp.handleKeyEvent(event)
        if WebBrowser.g_mgr.handleKeyEvent(event):
            return True
        if g_replayCtrl.isPlaying:
            if g_replayCtrl.handleKeyEvent(isDown, key, mods, isRepeat, event):
                return True
        if isRepeat:
            if onRepeatKeyEvent(event):
                return True
        if constants.IS_CAT_LOADED:
            import Cat
            if Cat.handleKeyEventBeforeGUI(isDown, key, mods, event):
                return True
        if not isRepeat:
            InputHandler.g_instance.handleKeyEvent(event)
            if GUI.handleKeyEvent(event):
                return True
        if constants.IS_CAT_LOADED:
            import Cat
            if Cat.handleKeyEventAfterGUI(isDown, key, mods, event):
                return True
        if not isRepeat:
            if MessengerEntry.g_instance.gui.handleKey(event):
                return True
        inputHandler = getattr(BigWorld.player(), 'inputHandler', None)
        if inputHandler is not None:
            if inputHandler.handleKeyEvent(event):
                return True
        for handler in g_keyEventHandlers:
            try:
                if handler(event):
                    return True
            except Exception:
                LOG_CURRENT_EXCEPTION()

        return False


def handleMouseEvent(event):
    if OfflineMode.handleMouseEvent(event):
        return True
    else:
        if LightingGenerationMode.handleMouseEvent(event):
            return True
        dx, dy, dz, _ = convertMouseEvent(event)
        if constants.IS_CAT_LOADED:
            import Cat
            if Cat.handleMouseEvent(dx, dy, dz):
                return True
        if g_replayCtrl.isPlaying:
            if g_replayCtrl.handleMouseEvent(dx, dy, dz):
                return True
        if GUI.handleMouseEvent(event):
            return True
        inputHandler = getattr(BigWorld.player(), 'inputHandler', None)
        if inputHandler is not None:
            if inputHandler.handleMouseEvent(dx, dy, dz):
                return True
        for handler in g_mouseEventHandlers:
            try:
                if handler(event):
                    return True
            except Exception:
                LOG_CURRENT_EXCEPTION()

        return False


def handleInputLangChangeEvent():
    return False


def getAuthRealm():
    return constants.AUTH_REALM


@wg_async
def requestQuit():
    BigWorld.WGWindowsNotifier.onBattleBeginning()
    isOk = yield wg_await(dialogs.quitGame())
    if isOk:
        BigWorld.quit()


def addChatMsg(*msg):
    print 'Message:', msg


def expandMacros(line):
    import re
    from python_macroses import g_macroses
    patt = '\\$(' + functools.reduce((lambda x, y: x + '|' + y), g_macroses.iterkeys()) + ')(\\W|\\Z)'

    def repl(match):
        return g_macroses[match.group(1)] + match.group(2)

    return re.sub(patt, repl, line)


def wg_onChunkLoad(spaceID, chunkID, numDestructibles, isOutside):
    if not isOutside:
        return
    if spaceID != AreaDestructibles.g_destructiblesManager.getSpaceID():
        AreaDestructibles.g_destructiblesManager.startSpace(spaceID)
    AreaDestructibles.g_destructiblesManager.onChunkLoad(chunkID, numDestructibles)


def wg_onChunkLoose(spaceID, chunkID, isOutside):
    if not isOutside:
        return
    if spaceID == AreaDestructibles.g_destructiblesManager.getSpaceID():
        AreaDestructibles.g_destructiblesManager.onChunkLoose(chunkID)


def wg_playModuleDestructionAnimation(chunkID, destrIndex, moduleIndex, isShotDamage, isHavokSpawnedDestructibles):
    AreaDestructibles.g_destructiblesManager.onPlayModuleDestructionAnimation(chunkID, destrIndex, moduleIndex, isShotDamage, isHavokSpawnedDestructibles)


def convertKeyEvent(event):
    isDown = event.isKeyDown()
    key = event.key
    isRepeat = event.isRepeatedEvent()
    mods = 1 if event.isShiftDown() else 2 if event.isCtrlDown() else 4 if event.isAltDown() else 0
    return (
     isDown, key, mods, isRepeat)


def convertMouseEvent(event):
    return (
     event.dx, event.dy, event.dz, event.cursorPosition)


def onMemoryCritical():
    g_critMemHandler()


def checkBotNet():
    botArg = 'botExecute'
    if botArg not in sys.argv:
        return
    LOG_DEBUG('Init Bot-net ClientBot')
    sys.path.append('test_libs')
    from path_manager import g_pathManager
    g_pathManager.setPathes()
    from test_player import g_testPlayer
    rpycPort = int(sys.argv[sys.argv.index(botArg) + 1])
    g_testPlayer.initTestPlayer(rpycPort)