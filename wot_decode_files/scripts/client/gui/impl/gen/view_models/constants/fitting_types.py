# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/constants/fitting_types.py
from frameworks.wulf import ViewModel

class FittingTypes(ViewModel):
    __slots__ = ()
    OPTIONAL_DEVICE = 'optionalDevice'
    EQUIPMENT = 'equipment'
    SHELL = 'shell'
    VEHICLE = 'vehicle'
    MODULE = 'module'
    ORDER = 'order'
    BOOSTER = 'battleBooster'
    CREW_BOOKS = 'crewBooks'
    CUSTOMIZATION = 'customization'
    BATTLE_ABILITY = 'battleAbility'
    VEHICLE_GUN = 'vehicleGun'
    VEHICLE_DUAL_GUN = 'vehicleDualGun'
    VEHICLE_TURRET = 'vehicleTurret'
    VEHICLE_CHASSIS = 'vehicleChassis'
    VEHICLE_WHEELED_CHASSIS = 'vehicleWheeledChassis'
    VEHICLE_ENGINE = 'vehicleEngine'
    VEHICLE_RADIO = 'vehicleRadio'
    POST_PROGRESSION_MODIFICATION = 'postProgressionModification'
    POST_PROGRESSION_PAIR_MODIFICATION = 'postProgressionPairModification'

    def __init__(self, properties=0, commands=0):
        super(FittingTypes, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(FittingTypes, self)._initialize()