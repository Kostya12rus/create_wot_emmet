# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gameplay/listeners.py
import weakref, BigWorld
from PlayerEvents import g_playerEvents
from constants import ARENA_GUI_TYPE
from frameworks.state_machine.events import StringEvent
from skeletons.gameplay import PlayerEventID, ReplayEventID

class PlayerEventsAdaptor(object):
    __slots__ = ('_machine', )

    def __init__(self, machine):
        super(PlayerEventsAdaptor, self).__init__()
        self._machine = weakref.proxy(machine)

    def startListening(self):
        g_playerEvents.onAccountBecomePlayer += self.__onAccountBecomePlayer
        g_playerEvents.onAccountBecomeNonPlayer += self.__onAccountBecomeNonPlayer
        g_playerEvents.onAvatarBecomePlayer += self.__onAvatarBecomePlayer
        g_playerEvents.onAvatarBecomeNonPlayer += self.__onAvatarBecomeNonPlayer
        g_playerEvents.onServerReplayEntering += self.__onServerReplayEntering
        g_playerEvents.onServerReplayExiting += self.__onServerReplayExiting

    def stopListening(self):
        g_playerEvents.onAccountBecomePlayer -= self.__onAccountBecomePlayer
        g_playerEvents.onAccountBecomeNonPlayer -= self.__onAccountBecomeNonPlayer
        g_playerEvents.onAvatarBecomePlayer -= self.__onAvatarBecomePlayer
        g_playerEvents.onAvatarBecomeNonPlayer -= self.__onAvatarBecomeNonPlayer
        g_playerEvents.onServerReplayEntering -= self.__onServerReplayEntering
        g_playerEvents.onServerReplayExiting -= self.__onServerReplayExiting

    def __onAccountBecomePlayer(self):
        self._machine.post(StringEvent(PlayerEventID.ACCOUNT_BECOME_PLAYER))

    def __onAccountBecomeNonPlayer(self):
        self._machine.post(StringEvent(PlayerEventID.ACCOUNT_BECOME_NON_PLAYER))

    def __onAvatarBecomePlayer(self):
        self._machine.post(StringEvent(PlayerEventID.AVATAR_BECOME_PLAYER, arenaGuiType=getattr(BigWorld.player(), 'arenaGuiType', ARENA_GUI_TYPE.UNKNOWN)))

    def __onAvatarBecomeNonPlayer(self):
        self._machine.post(StringEvent(PlayerEventID.AVATAR_BECOME_NON_PLAYER))

    def __onServerReplayEntering(self):
        self._machine.post(StringEvent(ReplayEventID.SERVER_REPLAY_ENTERING))

    def __onServerReplayExiting(self):
        self._machine.post(StringEvent(ReplayEventID.SERVER_REPLAY_EXITING))