# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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
    EQUIP_COIN_INFO_TOOLTIP = 'equipCoinInfo'
    TAB_SIMPLE = 'simple'
    TAB_MODERNIZED = 'modernized'

    def __init__(self, properties=0, commands=0):
        super(TankSetupConstants, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(TankSetupConstants, self)._initialize()