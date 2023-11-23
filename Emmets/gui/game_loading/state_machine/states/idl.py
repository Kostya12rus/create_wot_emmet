# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_loading/state_machine/states/idl.py
from frameworks.state_machine import State, StateFlags
import game_loading_bindings
from gui.game_loading import loggers
from gui.game_loading.state_machine.const import GameLoadingStates, LOADING_VIEW_FADE_OUT_DURATION
_logger = loggers.getStatesLogger()

class IdlState(State):
    __slots__ = ()

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(IdlState, self).__init__(stateID=GameLoadingStates.IDL.value, flags=flags)

    def _onEntered(self):
        super(IdlState, self)._onEntered()
        if game_loading_bindings.isViewOpened():
            _logger.debug('[%s] closing GF view.', self)
            game_loading_bindings.destroyLoadingView(LOADING_VIEW_FADE_OUT_DURATION)
        _logger.debug('[%s] entered.', self)