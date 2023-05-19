# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/dossiers2/custom/utils.py
from items import vehicles
import arena_achievements

def getVehicleNationID(vehTypeCompDescr):
    return vehicles.parseIntCompactDescr(vehTypeCompDescr)[1]


def isVehicleSPG(vehTypeCompDescr):
    itemTypeID, nationID, vehicleID = vehicles.parseIntCompactDescr(vehTypeCompDescr)
    return 'SPG' in vehicles.g_list.getList(nationID)[vehicleID].tags


def getInBattleSeriesIndex(seriesName):
    return arena_achievements.INBATTLE_SERIES_INDICES[seriesName]