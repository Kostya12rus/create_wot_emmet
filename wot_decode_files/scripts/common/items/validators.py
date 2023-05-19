# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/items/validators.py
from items import ITEM_TYPES, EQUIPMENT_TYPES, vehicles

def isBattleBooster(compDescr):
    itemTypeIdx, _, eqID = vehicles.parseIntCompactDescr(compDescr)
    if itemTypeIdx == ITEM_TYPES.equipment:
        equipment = vehicles.g_cache.equipments().get(eqID)
        if equipment and equipment.equipmentType == EQUIPMENT_TYPES.battleBoosters:
            return True
    return False