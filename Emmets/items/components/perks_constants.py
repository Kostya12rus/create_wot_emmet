# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/items/components/perks_constants.py
import typing
PERKS_XML_FILE = 'perks.xml'
PERK_BONUS_VALUE_PRECISION = 5
AVG_LVL_PERKS = ('loader_intuition', )

class PerkState(object):
    INACTIVE = 0
    ACTIVE = 1


class PerkTags(object):
    AUTOPERK = 4

    @classmethod
    def pack(cls, tags):
        return reduce(int.__or__, (getattr(cls, tag.upper()) for tag in tags), 0)


class PerkMasks(object):
    PERK_ID_MASK = 1023
    PERK_LEVEL_MASK = 63


class StubPerkIDs(object):
    COMMANDER_UNIVERSALIST = 102
    RADIOMAN_LAST_EFFORT = 504