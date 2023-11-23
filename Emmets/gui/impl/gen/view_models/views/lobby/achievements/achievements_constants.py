# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/achievements/achievements_constants.py
from enum import Enum
from frameworks.wulf import ViewModel

class KPITypes(Enum):
    BATTLES = 'battles'
    ASSISTANCE = 'assistance'
    DESTROYED = 'destroyed'
    BLOCKED = 'blocked'
    EXPERIENCE = 'experience'
    DAMAGE = 'damage'


class AchievementsConstants(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(AchievementsConstants, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(AchievementsConstants, self)._initialize()