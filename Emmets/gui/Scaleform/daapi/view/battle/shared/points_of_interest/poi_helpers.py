# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/points_of_interest/poi_helpers.py
import typing, BigWorld
from items import vehicles
from points_of_interest_shared import PoiEquipmentNamesByPoiType, PoiTypesByPoiEquipmentName
if typing.TYPE_CHECKING:
    from items.artefacts import Equipment
    from points_of_interest.components import PoiStateComponent

def getPoiCooldownProgress(poiState):
    status = poiState.status
    duration = status.endTime - status.startTime
    progress = (BigWorld.serverTime() - status.startTime) / duration * 100
    return progress


def getPoiEquipmentByType(poiType):
    cache = vehicles.g_cache
    name = PoiEquipmentNamesByPoiType[poiType]
    equipmentID = cache.equipmentIDs().get(name)
    if equipmentID is not None:
        return cache.equipments()[equipmentID]
    else:
        return


def getPoiTypeByEquipment(equipment):
    return PoiTypesByPoiEquipmentName.get(equipment.name, None)