# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/items/validators.py
from items import ITEM_TYPES, EQUIPMENT_TYPES, vehicles

def isBattleBooster(compDescr):
    itemTypeIdx, _, eqID = vehicles.parseIntCompactDescr(compDescr)
    if itemTypeIdx == ITEM_TYPES.equipment:
        equipment = vehicles.g_cache.equipments().get(eqID)
        if equipment and equipment.equipmentType == EQUIPMENT_TYPES.battleBoosters:
            return True
    return False