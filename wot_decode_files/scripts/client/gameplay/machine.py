# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gameplay/machine.py
import logging, BattleReplay
from constants import HAS_DEV_RESOURCES
from frameworks.state_machine import StateMachine
from gameplay import states
_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())

class GameplayStateMachine(StateMachine):
    __slots__ = ()

    @property
    def offline(self):
        return self.getChildByIndex(0)

    @property
    def online(self):
        return self.getChildByIndex(1)

    def configure(self):
        offline = states.OfflineState()
        offline.configure()
        online = states.OnlineState()
        online.configure(offline)
        self.addState(offline)
        self.addState(online)


class BattleReplayMachine(StateMachine):
    __slots__ = ()

    def configure(self):
        initialization = states.BattleReplayInitState()
        initialization.configure()
        playing = states.BattleReplayPlayingState()
        playing.configure(initialization)
        self.addState(initialization)
        self.addState(playing)

    def start(self, doValidate=True):
        super(BattleReplayMachine, self).start(doValidate)
        BattleReplay.g_replayCtrl.autoStartBattleReplay()


def create():
    if BattleReplay.g_replayCtrl.getAutoStartFileName():
        return BattleReplayMachine()
    if HAS_DEV_RESOURCES:
        try:
            from gui.development.dev_gameplay import DevGameplayStateMachine
        except ImportError:
            _logger.exception('Development state machine is not found')
            return GameplayStateMachine()

        return DevGameplayStateMachine()
    return GameplayStateMachine()