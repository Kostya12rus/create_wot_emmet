# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/vehicle_modules.py
import logging
from constants import SHELL_TYPES, SHELL_MECHANICS_TYPE
from gui.Scaleform.genConsts.FITTING_TYPES import FITTING_TYPES
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.RES_SHOP_EXT import RES_SHOP_EXT
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.items_parameters.params_cache import g_paramsCache
import nations
from items import vehicles as veh_core
from gui.shared.gui_items.fitting_item import FittingItem, ICONS_MASK
from gui.shared.utils import GUN_CLIP, GUN_CAN_BE_CLIP, GUN_AUTO_RELOAD, GUN_CAN_BE_AUTO_RELOAD, GUN_DUAL_GUN, GUN_CAN_BE_DUAL_GUN
from gui.shared.money import Currency
MODULE_TYPES_ORDER = ('vehicleGun', 'vehicleTurret', 'vehicleEngine', 'vehicleChassis',
                      'vehicleRadio', 'vehicleFuelTank')
MODULE_TYPES_ORDER_INDICES = dict((n, i) for i, n in enumerate(MODULE_TYPES_ORDER))
SHELL_TYPES_ORDER = (
 SHELL_TYPES.ARMOR_PIERCING, SHELL_TYPES.ARMOR_PIERCING_CR,
 SHELL_TYPES.HOLLOW_CHARGE, SHELL_TYPES.HIGH_EXPLOSIVE, SHELL_TYPES.SMOKE)
SHELL_TYPES_ORDER_INDICES = dict((n, i) for i, n in enumerate(SHELL_TYPES_ORDER))
_logger = logging.getLogger(__name__)

class VehicleModule(FittingItem):
    __slots__ = ('_vehicleModuleDescriptor', )

    def __init__(self, intCompactDescr, proxy=None, descriptor=None):
        super(VehicleModule, self).__init__(intCompactDescr, proxy)
        self._vehicleModuleDescriptor = descriptor

    @property
    def icon(self):
        return ''

    @property
    def descriptor(self):
        if self._vehicleModuleDescriptor is not None:
            return self._vehicleModuleDescriptor
        else:
            return super(VehicleModule, self).descriptor

    def _sortByType(self, other):
        return MODULE_TYPES_ORDER_INDICES[self.itemTypeName] - MODULE_TYPES_ORDER_INDICES[other.itemTypeName]

    def getGUIEmblemID(self):
        return self.itemTypeName

    def getShopIcon(self, size=STORE_CONSTANTS.ICON_SIZE_MEDIUM):
        return RES_SHOP_EXT.getModuleIcon(size, self.itemTypeName)


class VehicleChassis(VehicleModule):
    __slots__ = ()

    def isInstalled(self, vehicle, slotIdx=None):
        return self.intCD == vehicle.chassis.intCD

    def mayInstall(self, vehicle, slotIdx=None):
        installPossible, reason = FittingItem.mayInstall(self, vehicle, slotIdx)
        if not installPossible and reason == 'too heavy':
            return (False, 'too heavy chassis')
        return (installPossible, reason)

    def getInstalledVehicles(self, vehicles):
        result = set()
        for vehicle in vehicles:
            if self.intCD == vehicle.chassis.intCD:
                result.add(vehicle)

        return result

    def isHydraulicChassis(self):
        return g_paramsCache.isChassisHydraulic(self.intCD)

    def isWheeledChassis(self):
        return g_paramsCache.isChassisWheeled(self.intCD)

    def hasAutoSiege(self):
        return g_paramsCache.isChassisAutoSiege(self.intCD)

    def isTrackWithinTrack(self):
        return g_paramsCache.isTrackWithinTrack(self.intCD)

    @property
    def icon(self):
        if self.isWheeledChassis():
            return RES_ICONS.MAPS_ICONS_MODULES_WHEELEDCHASSIS
        return RES_ICONS.MAPS_ICONS_MODULES_CHASSIS

    def getBonusIcon(self, size='small'):
        if size == 'small':
            return self.icon
        if self.isWheeledChassis():
            return backport.image(R.images.gui.maps.icons.modules.wheeledChassisBig())
        return backport.image(R.images.gui.maps.icons.modules.chassisBig())

    def getExtraIconInfo(self, vehDescr=None):
        if self.isHydraulicChassis():
            if self.isWheeledChassis():
                return backport.image(R.images.gui.maps.icons.modules.hydraulicWheeledChassisIcon())
            return backport.image(R.images.gui.maps.icons.modules.hydraulicChassisIcon())
        else:
            if self.isTrackWithinTrack():
                return backport.image(R.images.gui.maps.icons.modules.trackWithinTrack())
            return

    def getGUIEmblemID(self):
        if self.isWheeledChassis():
            return FITTING_TYPES.VEHICLE_WHEELED_CHASSIS
        return super(VehicleChassis, self).getGUIEmblemID()

    def getShopIcon(self, size=STORE_CONSTANTS.ICON_SIZE_MEDIUM):
        if self.isWheeledChassis():
            return RES_SHOP_EXT.getModuleIcon(size, FITTING_TYPES.VEHICLE_WHEELED_CHASSIS)
        return super(VehicleChassis, self).getShopIcon(size)

    def _getShortInfoKey(self):
        return ('#menu:descriptions/{}').format(FITTING_TYPES.VEHICLE_WHEELED_CHASSIS if self.isWheeledChassis() else self.itemTypeName)


class VehicleTurret(VehicleModule):
    __slots__ = ()

    def isInstalled(self, vehicle, slotIdx=None):
        return self.intCD == vehicle.turret.intCD

    def mayInstall(self, vehicle, slotIdx=None, gunCD=0):
        if vehicle is None:
            return (False, 'not for current vehicle')
        else:
            optDevicesLayouts = None
            if vehicle.optDevices.setupLayouts.capacity > 1:
                optDevicesLayouts = []
                for setup in vehicle.optDevices.setupLayouts.setups.itervalues():
                    optDevicesLayouts.append(setup.getIntCDs())

            installPossible, reason = vehicle.descriptor.mayInstallTurret(self.intCD, gunCD, optDevicesLayouts=optDevicesLayouts)
            if not installPossible and reason == 'not for this vehicle type':
                return (False, 'need gun')
            return (
             installPossible, reason)

    def getInstalledVehicles(self, vehicles):
        result = set()
        for vehicle in vehicles:
            if self.intCD == vehicle.turret.intCD:
                result.add(vehicle)

        return result

    @property
    def icon(self):
        return RES_ICONS.MAPS_ICONS_MODULES_TOWER

    def getBonusIcon(self, size='small'):
        if size == 'small':
            return self.icon
        return backport.image(R.images.gui.maps.icons.modules.towerBig())

    @property
    def isGunCarriage(self):
        return self.descriptor.isGunCarriage


class VehicleGun(VehicleModule):
    __slots__ = ('_defaultAmmo', '_maxAmmo')

    def __init__(self, intCompactDescr, proxy=None, descriptor=None):
        super(VehicleGun, self).__init__(intCompactDescr, proxy, descriptor)
        self._defaultAmmo = self._getDefaultAmmo(proxy)
        self._maxAmmo = self._getMaxAmmo()

    def isInstalled(self, vehicle, slotIdx=None):
        return self.intCD == vehicle.gun.intCD

    def mayInstall(self, vehicle, slotIdx=None):
        installPossible, reason = FittingItem.mayInstall(self, vehicle)
        if not installPossible and reason == 'not for current vehicle':
            return (False, 'need turret')
        return (installPossible, reason)

    def getReloadingType(self, vehicleDescr=None):
        return g_paramsCache.getGunReloadingSystemType(self.intCD, vehicleDescr.type.compactDescr if vehicleDescr is not None else None)

    def isClipGun(self, vehicleDescr=None):
        typeToCheck = GUN_CLIP if vehicleDescr is not None else GUN_CAN_BE_CLIP
        return self.getReloadingType(vehicleDescr) == typeToCheck

    def isAutoReloadable(self, vehicleDescr=None):
        typeToCheck = GUN_AUTO_RELOAD if vehicleDescr is not None else GUN_CAN_BE_AUTO_RELOAD
        return self.getReloadingType(vehicleDescr) == typeToCheck

    def isDualGun(self, vehicleDescr=None):
        typeToCheck = GUN_DUAL_GUN if vehicleDescr is not None else GUN_CAN_BE_DUAL_GUN
        return self.getReloadingType(vehicleDescr) == typeToCheck

    def getInstalledVehicles(self, vehicles):
        result = set()
        for vehicle in vehicles:
            if self.intCD == vehicle.gun.intCD:
                result.add(vehicle)

        return result

    @property
    def defaultAmmo(self):
        return self._defaultAmmo

    @property
    def maxAmmo(self):
        return self._maxAmmo

    @property
    def icon(self):
        return RES_ICONS.MAPS_ICONS_MODULES_GUN

    def getBonusIcon(self, size='small'):
        if size == 'small':
            return self.icon
        return backport.image(R.images.gui.maps.icons.modules.gunBig())

    @property
    def userType(self):
        userType = super(VehicleGun, self).userType
        if self.isDualGun():
            return backport.text(R.strings.item_types.dualGun.name())
        return userType

    def getExtraIconInfo(self, vehDescr=None):
        if self.isClipGun(vehDescr):
            return backport.image(R.images.gui.maps.icons.modules.magazineGunIcon())
        else:
            if self.isAutoReloadable(vehDescr):
                if vehDescr:
                    for gun in vehDescr.type.getGuns():
                        if gun.compactDescr == self.intCD and gun.autoreloadHasBoost:
                            return backport.image(R.images.gui.maps.icons.modules.autoLoaderGunBoost())

                return backport.image(R.images.gui.maps.icons.modules.autoLoaderGun())
            if self.isDualGun(vehDescr):
                return backport.image(R.images.gui.maps.icons.modules.dualGun())
            return

    def getGUIEmblemID(self):
        if self.isDualGun():
            return FITTING_TYPES.VEHICLE_DUAL_GUN
        return super(VehicleGun, self).getGUIEmblemID()

    def _getMaxAmmo(self):
        return self.descriptor.maxAmmo

    def _getDefaultAmmo(self, proxy):
        result = []
        shells = veh_core.getDefaultAmmoForGun(self.descriptor)
        for i in range(0, len(shells), 2):
            result.append(Shell(shells[i], count=shells[(i + 1)], proxy=proxy))

        return result

    def _getShortInfoKey(self, vehicleDescr=None):
        key = super(VehicleGun, self)._getShortInfoKey()
        if self.isAutoReloadable(vehicleDescr):
            return ('/').join((key, 'autoReload'))
        if self.isDualGun(vehicleDescr):
            return ('/').join((key, 'dualGun'))
        return key


class VehicleEngine(VehicleModule):
    __slots__ = ()

    def isInstalled(self, vehicle, slotIdx=None):
        return self.intCD == vehicle.engine.intCD

    def getInstalledVehicles(self, vehicles):
        result = set()
        for vehicle in vehicles:
            if self.intCD == vehicle.engine.intCD:
                result.add(vehicle)

        return result

    def getConflictedEquipments(self, vehicle):
        conflictEqs = list()
        oldModuleId = vehicle.engine.intCD
        vehicle.descriptor.installComponent(self.intCD)
        for eq in vehicle.consumables.installed.getItems():
            installPossible, _ = eq.descriptor.checkCompatibilityWithVehicle(vehicle.descriptor)
            if not installPossible:
                conflictEqs.append(eq)

        vehicle.descriptor.installComponent(oldModuleId)
        return conflictEqs

    def hasTurboshaftEngine(self):
        return g_paramsCache.hasTurboshaftEngine(self.intCD)

    @property
    def icon(self):
        return RES_ICONS.MAPS_ICONS_MODULES_ENGINE

    def getBonusIcon(self, size='small'):
        if size == 'small':
            return self.icon
        return backport.image(R.images.gui.maps.icons.modules.engineBig())

    def getExtraIconInfo(self, vehDescr=None):
        if self.hasTurboshaftEngine():
            return RES_ICONS.MAPS_ICONS_MODULES_TURBINEENGINEICON
        else:
            return


class VehicleFuelTank(VehicleModule):
    __slots__ = ()

    def isInstalled(self, vehicle, slotIdx=None):
        return self.intCD == vehicle.fuelTank.intCD

    def getInstalledVehicles(self, vehicles):
        result = set()
        for vehicle in vehicles:
            if self.intCD == vehicle.fuelTank.intCD:
                result.add(vehicle)

        return result


class VehicleRadio(VehicleModule):
    __slots__ = ()

    def isInstalled(self, vehicle, slotIdx=None):
        return self.intCD == vehicle.radio.intCD

    def getInstalledVehicles(self, vehicles):
        result = set()
        for vehicle in vehicles:
            if self.intCD == vehicle.radio.intCD:
                result.add(vehicle)

        return result

    @property
    def icon(self):
        return RES_ICONS.MAPS_ICONS_MODULES_RADIO

    def getBonusIcon(self, size='small'):
        if size == 'small':
            return self.icon
        return backport.image(R.images.gui.maps.icons.modules.radioBig())


class Shell(FittingItem):
    __slots__ = ('_count', )

    def __init__(self, intCompactDescr, count=0, proxy=None, isBoughtForCredits=False):
        FittingItem.__init__(self, intCompactDescr, proxy, isBoughtForCredits)
        self._count = count

    @property
    def level(self):
        return 0

    @property
    def isModernMechanics(self):
        return self.type in (SHELL_TYPES.HIGH_EXPLOSIVE,) and self.descriptor.type.mechanics == SHELL_MECHANICS_TYPE.MODERN

    def _getAltPrice(self, buyPrice, proxy):
        if Currency.GOLD in buyPrice:
            return buyPrice.exchange(Currency.GOLD, Currency.CREDITS, proxy.exchangeRateForShellsAndEqs)
        return super(Shell, self)._getAltPrice(buyPrice, proxy)

    def _getFormatLongUserName(self, kind):
        if self.nationID == nations.INDICES['germany']:
            caliber = float(self.descriptor.caliber) / 10
            dimension = backport.text(R.strings.item_types.shell.dimension.sm())
        elif self.nationID == nations.INDICES['usa']:
            caliber = float(self.descriptor.caliber) / 25.4
            dimension = backport.text(R.strings.item_types.shell.dimension.inch())
        else:
            caliber = self.descriptor.caliber
            dimension = backport.text(R.strings.item_types.shell.dimension.mm())
        return backport.text(R.strings.item_types.shell.name(), kind=backport.text(R.strings.item_types.shell.dyn(kind).dyn(self.descriptor.kind)()), name=self.userName, caliber=backport.getNiceNumberFormat(caliber), dimension=dimension)

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value

    @property
    def type(self):
        return self.descriptor.kind

    @property
    def longUserName(self):
        return self._getFormatLongUserName('kinds')

    @property
    def longUserNameAbbr(self):
        return self._getFormatLongUserName('kindsAbbreviation')

    @property
    def icon(self):
        return ICONS_MASK[:-4] % {'type': self.itemTypeName, 
           'subtype': 'small/', 
           'unicName': self.descriptor.icon[0]}

    def getBonusIcon(self, size='small'):
        sizeFldr = R.images.gui.maps.icons.shell.dyn(size)
        if not sizeFldr:
            _logger.warn('Shell %s icon for size %s doesnt exists!', self.descriptor.iconName, size)
            return ''
        return backport.image(sizeFldr.dyn(self.descriptor.iconName)())

    def getShopIcon(self, size=STORE_CONSTANTS.ICON_SIZE_MEDIUM):
        return RES_SHOP_EXT.getShellIcon(size, self.descriptor.iconName)

    def getGUIEmblemID(self):
        return self.descriptor.iconName

    @property
    def defaultLayoutValue(self):
        return ((self.isBoughtForAltPrice or self).intCD if 1 else -self.intCD, self.count)

    def isInstalled(self, vehicle, slotIdx=None):
        for shell in vehicle.shells.installed.getItems():
            if self.intCD == shell.intCD:
                return True

        return super(Shell, self).isInstalled(vehicle, slotIdx)

    def isInSetup(self, vehicle, setupIndex=None, slotIdx=None):
        return vehicle.shells.setupLayouts.containsIntCD(self.intCD, setupIndex, slotIdx)

    def isInOtherLayout(self, vehicle):
        return vehicle.shells.setupLayouts.isInOtherLayout(self)

    def _sortByType(self, other):
        return SHELL_TYPES_ORDER_INDICES[self.type] - SHELL_TYPES_ORDER_INDICES[other.type]