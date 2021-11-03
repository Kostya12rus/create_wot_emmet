# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/mode_selector/mode_selector_window_states.py
from frameworks.wulf import ViewModel

class ModeSelectorWindowStates(ViewModel):
    __slots__ = ()
    NORMAL = 0
    BOOTCAMP = 1

    def __init__(self, properties=0, commands=0):
        super(ModeSelectorWindowStates, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(ModeSelectorWindowStates, self)._initialize()