# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/items/readers/__init__.py
from items.readers import chassis_readers
from items.readers import gun_readers
from items.readers import shared_readers
from items.readers import skills_readers
from items.readers import sound_readers
from items.readers import tankmen_readers
from constants import HAS_DEV_RESOURCES
try:
    from json_reader import vehicle_reader
except ImportError:
    vehicle_reader = None

__all__ = ('chassis_readers', 'gun_readers', 'shared_readers', 'skills_readers', 'sound_readers',
           'tankmen_readers', 'json_vehicle_reader')
if HAS_DEV_RESOURCES:
    json_vehicle_reader = vehicle_reader
else:
    json_vehicle_reader = None