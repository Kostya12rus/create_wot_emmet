# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle_royale/equipment_panel_cmp_rent_states.py
from frameworks.wulf import ViewModel

class EquipmentPanelCmpRentStates(ViewModel):
    __slots__ = ()
    STATE_NORMAL = 'normal'
    STATE_TEST_DRIVE_AVAILABLE = 'testDriveAvailable'
    STATE_TEST_DRIVE_ACTIVE = 'testDriveActive'
    STATE_RENT_AVAILABLE = 'rentAvailable'
    STATE_RENT_ACTIVE = 'rentActive'

    def __init__(self, properties=0, commands=0):
        super(EquipmentPanelCmpRentStates, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(EquipmentPanelCmpRentStates, self)._initialize()