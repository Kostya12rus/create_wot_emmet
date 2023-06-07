# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/points_of_interest_shared.py
import enum
ENEMY_VEHICLE_ID = -1
INVALID_TIMESTAMP = -1
POI_EQUIPMENT_TAG = 'poiEquipment'

@enum.unique
class PoiType(enum.IntEnum):
    ARTILLERY = 1
    RECON = 2


@enum.unique
class PoiStatus(enum.IntEnum):
    ACTIVE = 1
    CAPTURING = 2
    COOLDOWN = 3


@enum.unique
class PoiBlockReasons(enum.IntEnum):
    DAMAGE = 1
    EQUIPMENT = 2
    OVERTURNED = 3


PoiEquipmentNamesByPoiType = {PoiType.ARTILLERY: 'poi_artillery_aoe', 
   PoiType.RECON: 'poi_radar'}
PoiTypesByPoiEquipmentName = {name: poiType for poiType, name in PoiEquipmentNamesByPoiType.iteritems()}