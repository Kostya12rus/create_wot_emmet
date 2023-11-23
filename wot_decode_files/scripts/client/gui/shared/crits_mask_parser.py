# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/crits_mask_parser.py
from shared_utils import BitmaskHelper
from shared_utils import CONST_CONTAINER
from items.vehicles import VEHICLE_DEVICE_TYPE_NAMES, VEHICLE_TANKMAN_TYPE_NAMES

class CRIT_MASK_SUB_TYPES(CONST_CONTAINER):
    DESTROYED_DEVICES = 'destroyedDevices'
    CRITICAL_DEVICES = 'criticalDevices'
    DESTROYED_TANKMENS = 'destroyedTankmen'


def critsParserGenerator(mask):
    mask = mask & -257
    maskMap = {CRIT_MASK_SUB_TYPES.DESTROYED_DEVICES: (
                                             mask >> 12 & 4095, VEHICLE_DEVICE_TYPE_NAMES), 
       CRIT_MASK_SUB_TYPES.CRITICAL_DEVICES: (
                                            mask & 4095, VEHICLE_DEVICE_TYPE_NAMES), 
       CRIT_MASK_SUB_TYPES.DESTROYED_TANKMENS: (
                                              mask >> 24 & 255, VEHICLE_TANKMAN_TYPE_NAMES)}
    for subType, (subMask, types) in maskMap.iteritems():
        if subMask > 0:
            for index in BitmaskHelper.iterateInt64SetBitsIndexes(subMask):
                yield (
                 subType, types[index])