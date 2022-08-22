# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/genConsts/FITTING_TYPES.py


class FITTING_TYPES(object):
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
    STORE_SLOTS = [VEHICLE, MODULE, SHELL, OPTIONAL_DEVICE, EQUIPMENT, BOOSTER]
    ARTEFACT_SLOTS = [OPTIONAL_DEVICE, EQUIPMENT]
    VEHICLE_GUN = 'vehicleGun'
    VEHICLE_DUAL_GUN = 'vehicleDualGun'
    VEHICLE_TURRET = 'vehicleTurret'
    VEHICLE_CHASSIS = 'vehicleChassis'
    VEHICLE_WHEELED_CHASSIS = 'vehicleWheeledChassis'
    VEHICLE_ENGINE = 'vehicleEngine'
    VEHICLE_RADIO = 'vehicleRadio'
    MANDATORY_SLOTS = [VEHICLE_GUN, VEHICLE_TURRET, VEHICLE_CHASSIS, VEHICLE_ENGINE, VEHICLE_RADIO]
    VEHICLE_GUN_OVERRIDE = [VEHICLE_GUN, VEHICLE_DUAL_GUN]
    VEHICLE_CHASSIS_OVERRIDE = [VEHICLE_CHASSIS, VEHICLE_WHEELED_CHASSIS]
    MANDATORY_SLOTS_OVERRIDES = [VEHICLE_GUN_OVERRIDE, VEHICLE_CHASSIS_OVERRIDE]
    RESERVE_SLOT1 = 'reserveSlot1'
    RESERVE_SLOT2 = 'reserveSlot2'
    RESERVE_SLOT3 = 'reserveSlot3'
    RESERVES_SLOTS = [RESERVE_SLOT1, RESERVE_SLOT2, RESERVE_SLOT3]
    TARGET_OTHER = 'other'
    TARGET_HANGAR = 'hangar'
    TARGET_HANGAR_CANT_INSTALL = 'hangarCantInstall'
    TARGET_HANGAR_DUPLICATE = 'hangarDuplicate'
    TARGET_VEHICLE = 'vehicle'
    ITEM_TARGETS = [TARGET_OTHER, TARGET_HANGAR, TARGET_HANGAR_CANT_INSTALL, TARGET_VEHICLE]
    GUN_TURRET_FITTING_ITEM_RENDERER = 'GunTurretFittingItemRendererUI'
    RESERVE_FITTING_ITEM_RENDERER = 'ReserveFittingItemRendererUI'
    RESERVE_PARAMS_ITEM_RENDERER = 'ReserveParamsItemRendererUI'
    ENGINE_FITTING_ITEM_RENDERER = 'EngineFittingItemRendererUI'
    ENGINE_FITTING_BIG_ITEM_RENDERER = 'EngineFittingBigItemRendererUI'
    RADIO_FITTING_ITEM_RENDERER = 'RadioFittingItemRendererUI'
    CHASSIS_FITTING_ITEM_RENDERER = 'ChassisFittingItemRendererUI'
    FITTING_RENDERERS = [GUN_TURRET_FITTING_ITEM_RENDERER, RESERVE_FITTING_ITEM_RENDERER, ENGINE_FITTING_ITEM_RENDERER, ENGINE_FITTING_BIG_ITEM_RENDERER, RADIO_FITTING_ITEM_RENDERER, CHASSIS_FITTING_ITEM_RENDERER]
    MODULE_FITTING_RENDERER_DATA_CLASS_NAME = 'net.wg.gui.lobby.modulesPanel.data.ModuleVO'
    HANGAR_POPOVER_TOP_MARGIN = 80
    VEHPREVIEW_POPOVER_MIN_AVAILABLE_HEIGHT = 575
    LARGE_POPOVER_WIDTH = 540
    MEDUIM_POPOVER_WIDTH = 500
    SHORT_POPOVER_WIDTH = 440
    RESERVE_POPOVER_WIDTH = 480