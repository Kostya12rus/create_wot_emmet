# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/bootcamp/states/StateInitial.py
from bootcamp.states import STATE
from bootcamp.states.AbstractState import AbstractState

class StateInitial(AbstractState):

    def __init__(self):
        super(StateInitial, self).__init__(STATE.INITIAL)

    def handleKeyEvent(self, event):
        pass

    def _doActivate(self):
        pass

    def _doDeactivate(self):
        pass