# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/bootcamp_shared.py


class BOOTCAMP_BATTLE_ACTION(object):
    PLAYER_MOVE = 0
    PLAYER_SHOOT = 1
    PLAYER_SPOTTED = 2
    PLAYER_HIT_VEHICLE = 3
    PLAYER_OBSERVED_ACTION = 4
    SET_SCENERY_CONSTANT = 5


class BOOTCAMP_START_TYPE(object):
    AUTOMATICALLY = 0
    PLAYER_CHOICE = 1
    PLAYER_MANUAL = 2


class PLAYER_COHORT_TYPE(object):
    NEW_PLAYER = 0
    WOT_RETURN_PLAYER = 1
    WOT_PLAYER = 2