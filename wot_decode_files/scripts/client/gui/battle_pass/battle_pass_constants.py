# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_pass/battle_pass_constants.py
from enum import Enum, unique
MIN_LEVEL = 1

class BonusesLayoutConsts(object):
    PRIORITY_KEY = 'priority'
    VISIBILITY_KEY = 'isVisible'
    OVERRIDE_KEY = 'override'
    ID_KEY = 'id'
    LEVEL_KEY = 'level'
    BIG_ICON_KEY = 'bigIcon'
    MAIN_KEYS = (
     PRIORITY_KEY, VISIBILITY_KEY, BIG_ICON_KEY)
    INT_VALUES = (PRIORITY_KEY,)
    BOOL_VALUES = (VISIBILITY_KEY,)


@unique
class ChapterState(Enum):
    ACTIVE = 'active'
    PAUSED = 'paused'
    COMPLETED = 'completed'
    NOT_STARTED = 'notStarted'