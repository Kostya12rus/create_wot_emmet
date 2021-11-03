# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/nation_change_helpers/client_nation_change_helper.py
from helpers import dependency
from nation_change.nation_change_helpers import iterVehTypeCDsInNationGroup, isMainInNationGroup
from skeletons.gui.shared import IItemsCache

def getValidVehicleCDForNationChange(vehCompDescr):
    tempVehCD = vehCompDescr
    vehicle = _getItem(vehCompDescr)
    if vehicle.hasNationGroup:
        if vehicle.isInInventory:
            if not vehicle.activeInNationGroup:
                tempVehCD = iterVehTypeCDsInNationGroup(vehCompDescr).next()
        elif not isMainInNationGroup(vehCompDescr):
            tempVehCD = iterVehTypeCDsInNationGroup(vehCompDescr).next()
    return tempVehCD


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def _getItem(itemID, itemsCache=None):
    return itemsCache.items.getItemByCD(itemID)