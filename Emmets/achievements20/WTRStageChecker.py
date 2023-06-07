# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/achievements20/WTRStageChecker.py
from bisect import bisect_right

class WTRStageChecker(object):
    __slots__ = [
     '_flatStages', '_stagesRatingsCache']

    def __init__(self, wtrStages):
        self._flatStages = [ (groupIndex + 1, stageIndex + 1, startRating) for groupIndex, group in enumerate(wtrStages) for stageIndex, startRating in enumerate(group)
                           ]
        self._stagesRatingsCache = tuple(wtrStage[2] for wtrStage in self._flatStages)

    def getStage(self, wtr):
        index = bisect_right(self._stagesRatingsCache, wtr) - 1
        if index < 0:
            return None
        else:
            return self._flatStages[index]