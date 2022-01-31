# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/items/components/lunar_ny_constants.py
import enum
INVALID_CHARM_ID = -1

class CharmType(object):
    COMMON = 'common'
    RARE = 'rare'
    ALL = (
     COMMON, RARE)


class CharmBonusMsk(object):
    NONE = 0
    CREDITS = 1
    XP = 2
    FREE_XP = 4
    TANKMEN_XP = 8
    ALL = NONE | CREDITS | XP | FREE_XP | TANKMEN_XP

    @classmethod
    def getMskByName(cls, name, default=NONE):
        return getattr(cls, name, default)


class CharmBonuses(enum.Enum):
    CREDITS = 'creditsFactor'
    XP = 'xpFactor'
    FREE_XP = 'freeXPFactor'
    TANKMEN_XP = 'tankmenXPFactor'

    @classmethod
    def getDefaultBonuses(cls, default=0.0):
        return {bonus.value:default for bonus in cls}