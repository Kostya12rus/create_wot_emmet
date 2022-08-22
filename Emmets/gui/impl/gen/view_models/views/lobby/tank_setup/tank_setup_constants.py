# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/tank_setup_constants.py
from frameworks.wulf import ViewModel

class TankSetupConstants(ViewModel):
    __slots__ = ()
    OPT_DEVICES = 'optDevices'
    SHELLS = 'shells'
    CONSUMABLES = 'consumables'
    BATTLE_BOOSTERS = 'battleBoosters'
    BATTLE_ABILITIES = 'battleAbilities'
    TOGGLE_SHELLS = 'toggleShells'
    TOGGLE_CAMOUFLAGE = 'toggleCamouflage'
    EMPTY = ''
    APPLY_DEFAULT = 'apply'
    APPLY_VEHICLE = 'applyVehicle'
    APPLY_TYPE = 'applyType'
    SPECIAL_SETUP_INFO_SLOT_TOOLTIP = 'specialSetupInfoSlotTooltip'

    def __init__(self, properties=0, commands=0):
        super(TankSetupConstants, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(TankSetupConstants, self)._initialize()