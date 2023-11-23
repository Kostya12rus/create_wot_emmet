# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/epic/status_notifications/epic_helpers.py
from items import vehicles

def getEquipmentById(equipmentId):
    return vehicles.g_cache.equipments()[equipmentId]


def getSmokeDataByPredicate(smokeInfo, teamPredicate, postEffectPredicate):
    if smokeInfo is None or not teamPredicate or not postEffectPredicate:
        return (None, None)
    if teamPredicate(smokeInfo['team']) and postEffectPredicate(smokeInfo['expiring']):
        return (smokeInfo['endTime'], getEquipmentById(smokeInfo['equipmentID']))
    else:
        return (None, None)