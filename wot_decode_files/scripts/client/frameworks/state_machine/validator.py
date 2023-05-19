# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/frameworks/state_machine/validator.py
from . import states as _states
from . import visitor
from .exceptions import StateMachineError
from .transitions import BaseTransition

def _validateTransition(transition, upper=None):
    source = transition.getSource()
    if source is None:
        raise StateMachineError(('{} has no source').format(transition))
    targets = transition.getTargets()
    if not targets:
        raise StateMachineError(('{} has no targets').format(transition))
    if visitor.getLCA([source] + targets, upper=upper) is None:
        raise StateMachineError(('States have no LCA in {}').format(transition))
    return


def _validateInitialState(state):
    initial = state.getInitial()
    if initial is None:
        raise StateMachineError(('{} has no initial state').format(state))
    return


def _validateState(state, machine):
    if state.isCompound():
        _validateInitialState(state)
    if state.isHistory() and len(state.getTransitions()) > 1:
        raise StateMachineError(('History state {} should have only one transition').format(state))
    if not state.isFinal():
        for transition in state.getTransitions():
            _validateTransition(transition, upper=machine.getParent())


def validate(machine):
    _validateInitialState(machine)
    ids = []
    for state in machine.visitInOrder((lambda item: isinstance(item, _states.State))):
        if state.isMachine():
            if state != machine:
                validate(state)
        else:
            stateID = state.getStateID()
            if stateID:
                if stateID not in ids:
                    ids.append(stateID)
                else:
                    raise StateMachineError(('{} is not unique, each state must have unique ID').format(state))
            _validateState(state, machine)