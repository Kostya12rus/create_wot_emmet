# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/new_year/views/craft/ny_craft_states.py
from frameworks.wulf import ViewModel

class NyCraftStates(ViewModel):
    __slots__ = ()
    CRAFT_REGULAR = 0
    CRAFT_MEGA = 1
    CRAFT_REGULAR_WITH_FILLER = 2

    def __init__(self, properties=0, commands=0):
        super(NyCraftStates, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(NyCraftStates, self)._initialize()