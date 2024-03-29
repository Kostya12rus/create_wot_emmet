# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/items/combined_crew_skill.py
from typing import Optional
from items import tankmen

class CombinedCrewSkill(object):
    __slots__ = ('tankmanLevel', 'levelIncrease', 'isTankmanActive', 'hasActiveTankmanForBooster',
                 'boosterMultiplier')

    def __init__(self, tankmanLevel, levelIncrease, isTankmanActive, hasActiveTankmanForBooster=False, boosterMultiplier=None):
        self.tankmanLevel = tankmanLevel
        self.levelIncrease = levelIncrease
        self.isTankmanActive = isTankmanActive
        self.hasActiveTankmanForBooster = hasActiveTankmanForBooster
        self.boosterMultiplier = boosterMultiplier

    @property
    def level(self):
        return int(round(self._floatLevel()))

    def _floatLevel(self):
        if self.boosterMultiplier is None:
            return self.tankmanLevel + self.levelIncrease
        else:
            if self.tankmanLevel < tankmen.MAX_SKILL_LEVEL or not self.isTankmanActive:
                return tankmen.MAX_SKILL_LEVEL + self.levelIncrease
            return (tankmen.MAX_SKILL_LEVEL + self.levelIncrease) * self.boosterMultiplier

    @property
    def isActive(self):
        return self.isTankmanActive or self.boosterMultiplier is not None and self.hasActiveTankmanForBooster

    def __str__(self):
        return ('CombinedCrewSkill(level={}, isActive={}, tankmanLevel={}, levelIncrease={}, isTankmanActive={}, boosterMultiplier={})').format(self.level, self.isActive, self.tankmanLevel, self.levelIncrease, self.isTankmanActive, self.boosterMultiplier)