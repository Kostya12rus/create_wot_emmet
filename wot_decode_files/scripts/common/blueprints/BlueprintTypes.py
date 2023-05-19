# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/blueprints/BlueprintTypes.py
from wotdecorators import singleton

@singleton
class BlueprintTypes(object):
    NONE = 0
    VEHICLE = 1
    NATIONAL = 2
    INTELLIGENCE_DATA = 3
    UNIVERSAL = (
     NATIONAL, INTELLIGENCE_DATA)
    ALL = (NATIONAL, VEHICLE, INTELLIGENCE_DATA)