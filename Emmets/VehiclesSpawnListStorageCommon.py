# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/VehiclesSpawnListStorageCommon.py
from collections import namedtuple
VehicleSpawnData = namedtuple('VehicleSpawnData', ['vehicleCD', 'outfitCD'])

def convertVehicleSpawnDataToTuples(spawnData):
    return {(data.vehicleCD, data.outfitCD) for data in spawnData}


def convertTuplesToVehicleSpawnData(tuples):
    return {VehicleSpawnData(data[0], data[1]) for data in tuples}