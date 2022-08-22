# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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