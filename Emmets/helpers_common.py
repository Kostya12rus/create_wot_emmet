# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/helpers_common.py
from constants import DeviceRepairMode
DEVICE_SLOWED_REPAIR_MASK = 128

def packDeviceRepairProgress(progress, repairMode):
    if repairMode != DeviceRepairMode.NORMAL:
        return progress | DEVICE_SLOWED_REPAIR_MASK
    return progress


def unpackDeviceRepairProgress(progressData):
    return (
     progressData & ~DEVICE_SLOWED_REPAIR_MASK,
     bool(progressData & DEVICE_SLOWED_REPAIR_MASK))