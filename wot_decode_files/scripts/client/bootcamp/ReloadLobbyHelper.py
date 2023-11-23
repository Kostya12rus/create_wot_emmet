# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/bootcamp/ReloadLobbyHelper.py
from gui.shared import events, g_eventBus, EVENT_BUS_SCOPE
from helpers import aop, dependency
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.game_control import IGameStateTracker

class _PointcutGameSessionControllerFix(aop.Pointcut):

    def __init__(self):
        super(_PointcutGameSessionControllerFix, self).__init__('gui.game_control.GameSessionController', 'GameSessionController', '_stop', aspects=(
         _AspectGameSessionControllerFix,))


class _AspectGameSessionControllerFix(aop.Aspect):

    def atCall(self, cd):
        return cd.changeArgs((
         0, 'doNotifyInStart', False))


class ReloadLobbyHelper(object):
    appLoader = dependency.descriptor(IAppLoader)
    gameState = dependency.descriptor(IGameStateTracker)

    def __init__(self):
        super(ReloadLobbyHelper, self).__init__()
        self.__isReloading = False

    def cancel(self):
        if self.__isReloading:
            g_eventBus.removeListener(events.GUICommonEvent.LOBBY_VIEW_LOADED, self.__onLobbyViewLoaded, EVENT_BUS_SCOPE.DEFAULT)
        self.__isReloading = False

    def reload(self):
        self.__isReloading = True
        g_eventBus.addListener(events.GUICommonEvent.LOBBY_VIEW_LOADED, self.__onLobbyViewLoaded, EVENT_BUS_SCOPE.DEFAULT)
        from gui.prb_control.dispatcher import g_prbLoader
        pc = _PointcutGameSessionControllerFix()
        g_prbLoader.onAccountBecomeNonPlayer()
        self.gameState.onAvatarBecomePlayer()
        self.appLoader.switchAccountEntity()
        g_prbLoader.onAccountShowGUI({})
        pc.clear()

    def __onLobbyViewLoaded(self, _):
        self.cancel()