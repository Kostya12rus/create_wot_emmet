# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/core/logger.py
import typing, BattleReplay
from gui.shared.utils import getPlayerDatabaseID
from helpers import dependency
from helpers.log.adapters import getWithContext
from skeletons.connection_mgr import IConnectionManager
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.ui_logging import IUILoggingCore
from PlayerEvents import g_playerEvents as playerEvents
from bootcamp.BootCampEvents import g_bootcampEvents as bootcampPlayerEvents
from wotdecorators import noexcept
from uilogging.constants import DEFAULT_LOGGER_NAME, LogLevels
from uilogging.core.common import convertEnum
from uilogging.core.core_constants import ENSURE_SESSION_TICK
from uilogging.core.log import LogRecord
from uilogging.core.handler import LogHandler, Delayer
from uilogging.deprecated.bootcamp.log_record import BootcampLogRecord
from uilogging.deprecated.logging_constants import FEATURES
if typing.TYPE_CHECKING:
    from uilogging.types import FeatureType, GroupType, ActionType, LogLevelType

class UILoggingCore(IUILoggingCore):
    _connectionMgr = dependency.descriptor(IConnectionManager)
    _lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self):
        self._handler = None
        self._started = False
        self._ensureSession = False
        self._sessionKeeper = None
        self._logger = getWithContext(DEFAULT_LOGGER_NAME, self)
        return

    def init(self):
        playerEvents.onAccountShowGUI += self._start
        bootcampPlayerEvents.onAccountShowGUI += self._start
        playerEvents.onAvatarReady += self._start
        self._connectionMgr.onDisconnected += self._stop
        self._logger.debug('Initialized.')

    def fini(self):
        playerEvents.onAccountShowGUI -= self._start
        bootcampPlayerEvents.onAccountShowGUI -= self._start
        playerEvents.onAvatarReady -= self._start
        self._connectionMgr.onDisconnected -= self._stop
        self._stop()
        self._logger.debug('Destroyed.')

    def ensureSession(self):
        self._ensureSession = True
        self._startSessionKeeper()

    def isFeatureEnabled(self, feature):
        if not self._isEnabled:
            return False
        return self._handler.isFeatureEnabled(convertEnum(feature))

    @noexcept
    def log(self, feature, group, action, loglevel=LogLevels.INFO, **params):
        if not self._isEnabled:
            return
        record = BootcampLogRecord if feature == FEATURES.BOOTCAMP else LogRecord
        log = record(feature=feature, group=group, action=action, level=loglevel, params=params)
        if log.broken:
            self._logger.warning('Broken %s.', log)
            return
        self._handler.add(log)

    @property
    def _disabled(self):
        return not self._lobbyContext.getServerSettings().uiLogging.enabled

    @property
    def _isEnabled(self):
        if self._disabled or not self._handler:
            self._logger.debug('[disabled=%s|destroyed=%s] Disabled.', self._disabled, not self._handler)
            return False
        if BattleReplay.isPlaying():
            self._logger.debug('Watching replay. Disabled.')
            return False
        return True

    def _start(self, *args, **kwargs):
        if self._started:
            self._startSessionKeeper()
            self._logger.debug('Already started.')
            return
        playerID = getPlayerDatabaseID()
        self._logger.debug('Got player id: %s.', playerID)
        if not playerID:
            self._logger.warning('No player id, start failed.')
            return
        self._handler = LogHandler(playerID)
        self._handler.onDestroy += self._shutdown
        self._started = True
        self._startSessionKeeper()
        self._logger.debug('Started.')

    def _stop(self, *args, **kwargs):
        self._shutdown()
        self._started = False
        self._logger.debug('Stopped.')

    def _shutdown(self):
        self._ensureSession = False
        self._stopSessionKeeper()
        if self._handler:
            self._handler.onDestroy -= self._shutdown
            self._logger.debug('Shutdown.')
            if not self._handler.destroyed:
                self._handler.destroy(flush=True)
        self._handler = None
        return

    def _getSessionLifetime(self):
        lifetime = None
        if self._isEnabled:
            lifetime = self._handler.getSessionLifetime()
            if lifetime is not None:
                lifetime = max(lifetime, ENSURE_SESSION_TICK)
        self._logger.debug('Session keeper next tick = %s.', lifetime)
        if lifetime is None:
            self._stopSessionKeeper()
        return lifetime

    def _startSessionKeeper(self, *args, **kwargs):
        if self._sessionKeeper is None and self._ensureSession and self._isEnabled:
            self._sessionKeeper = Delayer(ENSURE_SESSION_TICK, self._getSessionLifetime)
            self._logger.debug('Session keeper started.')
        return

    def _stopSessionKeeper(self):
        if self._sessionKeeper is not None:
            self._sessionKeeper.destroy()
            self._sessionKeeper = None
            self._logger.debug('Session keeper stopped.')
        return