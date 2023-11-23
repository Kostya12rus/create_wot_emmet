# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/animated_hints/constants.py
import enum

class HintType(enum.IntEnum):
    Move = 1
    MoveTurret = 2
    Shoot = 3
    SniperOnDistance = 4
    SniperLevel0 = 5
    AdvancedSniper = 6
    WeakPoints = 7
    TargetLock = 8


class EventAction(enum.IntEnum):
    Show = 1
    Hide = 2
    Complete = 3
    Close = 4
    SetPenetration = 5


LOGGER_NAME = 'animated_hints'