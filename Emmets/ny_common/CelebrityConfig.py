# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/ny_common/CelebrityConfig.py
from typing import Optional
from ny_common.settings import CelebrityConsts

class CelebrityConfig(object):
    __slots__ = ('_config', )

    def __init__(self, config):
        self._config = config

    def getSimplificationCosts(self):
        return self._config.get(CelebrityConsts.SIMPLIFICATION_COSTS, {})

    def calculateSimplificationCost(self, fromLevel, toLevel):
        if toLevel > fromLevel:
            return None
        else:
            costs = self.getSimplificationCosts()
            resultCost = 0
            for level in xrange(fromLevel, toLevel, -1):
                resultCost += costs.get(level, 0)

            return resultCost

    def getQuestCount(self):
        return self._config.get(CelebrityConsts.QUEST_COUNT, 0)