# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/premacc/maps_blacklist_slot_states.py
from frameworks.wulf import ViewModel

class MapsBlacklistSlotStates(ViewModel):
    __slots__ = ()
    MAPS_BLACKLIST_SLOT_STATE_ACTIVE = 'active'
    MAPS_BLACKLIST_SLOT_STATE_CHANGE = 'change'
    MAPS_BLACKLIST_SLOT_STATE_DISABLED = 'disabled'
    MAPS_BLACKLIST_SLOT_STATE_COOLDOWN = 'cooldown'
    MAPS_BLACKLIST_SLOT_STATE_SELECTED = 'selected'
    MAPS_BLACKLIST_SLOT_STATE_ACTIVE_NO_HOVER = 'active_no_hover'

    def __init__(self, properties=0, commands=0):
        super(MapsBlacklistSlotStates, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(MapsBlacklistSlotStates, self)._initialize()