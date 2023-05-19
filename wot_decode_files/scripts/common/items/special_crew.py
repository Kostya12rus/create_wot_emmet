# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/items/special_crew.py
import typing
from items import tankmen
from items.components.tankmen_components import SPECIAL_CREW_TAG
if typing.TYPE_CHECKING:
    from items.vehicles import VehicleType

def isSabatonCrew(tankmanDescr):
    return _hasTagInTankmenGroup(tankmanDescr, SPECIAL_CREW_TAG.SABATON)


def isOffspringCrew(tankmanDescr):
    return _hasTagInTankmenGroup(tankmanDescr, SPECIAL_CREW_TAG.OFFSPRING)


def isYhaCrew(tankmanDescr):
    return _hasTagInTankmenGroup(tankmanDescr, SPECIAL_CREW_TAG.YHA)


def isWitchesCrew(tankmanDescr):
    return _hasTagInTankmenGroup(tankmanDescr, SPECIAL_CREW_TAG.WITCHES_CREW)


def isMihoCrewCompleted(vehicleType, tankmenGroups):
    return _isCrewCompleted(vehicleType, tankmenGroups, SPECIAL_CREW_TAG.MIHO)


def isYhaCrewCompleted(vehicleType, tankmenGroups):
    return _isCrewCompleted(vehicleType, tankmenGroups, SPECIAL_CREW_TAG.YHA)


def isWitchesCrewCompleted(vehicleType, tankmenGroups):
    _, _, isPremium = tankmen.unpackCrewParams(tankmenGroups[0])
    nationID, _ = vehicleType.id
    requiredGroupIDs = tankmen.getTankmenWithTag(nationID, isPremium, SPECIAL_CREW_TAG.WITCHES_CREW)
    uniqueRoles = set([ role[0] for role in vehicleType.crewRoles ])
    actualGroupIDs = set([ tankmen.unpackCrewParams(tGroup)[0] for tGroup in tankmenGroups ])
    return len(actualGroupIDs & requiredGroupIDs) == len(uniqueRoles)


def _hasTagInTankmenGroup(tankmanDescr, tag):
    return tankmen.hasTagInTankmenGroup(tankmanDescr.nationID, tankmanDescr.gid, tankmanDescr.isPremium, tag)


def _isCrewCompleted(vehicleType, tankmenGroups, tag):
    _, _, isPremium = tankmen.unpackCrewParams(tankmenGroups[0])
    nationID, _ = vehicleType.id
    requiredCrew = tankmen.getTankmenWithTag(nationID, isPremium, tag)
    actualCrew = [ tankmen.unpackCrewParams(tGroup)[0] for tGroup in tankmenGroups ]
    if len(actualCrew) <= len(requiredCrew):
        return set(actualCrew) <= requiredCrew
    return requiredCrew < set(actualCrew)