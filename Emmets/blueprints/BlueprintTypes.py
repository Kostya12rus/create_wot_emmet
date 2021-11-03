# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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