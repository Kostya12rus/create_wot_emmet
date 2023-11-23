# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/VehiclesSpawnListStorageCommon.py
from collections import namedtuple
VehicleSpawnData = namedtuple('VehicleSpawnData', ['vehicleCD', 'outfitCD'])

def convertVehicleSpawnDataToTuples(spawnData):
    return {(data.vehicleCD, data.outfitCD) for data in spawnData}


def convertTuplesToVehicleSpawnData(tuples):
    return {VehicleSpawnData(data[0], data[1]) for data in tuples}