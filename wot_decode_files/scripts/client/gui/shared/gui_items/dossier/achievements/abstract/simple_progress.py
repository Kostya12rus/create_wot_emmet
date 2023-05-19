# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/abstract/simple_progress.py
from regular import RegularAchievement
from dossiers2.custom.config import RECORD_CONFIGS

class SimpleProgressAchievement(RegularAchievement):
    __slots__ = ('_progressValue', )

    def __init__(self, name, block, dossier, value=None):
        if dossier is not None:
            self._progressValue = self._readProgressValue(dossier)
        else:
            self._progressValue = 0
        super(SimpleProgressAchievement, self).__init__(name, block, dossier, value)
        return

    def getProgressValue(self):
        if not self._lvlUpTotalValue:
            return 1.0
        return 1 - float(self._lvlUpValue) / float(self._lvlUpTotalValue)

    def isInNear(self):
        return self.getProgressValue() > 0

    def hasProgress(self):
        return not self._isDone

    def _readLevelUpValue(self, dossier):
        minValue = RECORD_CONFIGS[self._name]
        medals, series = divmod(self._progressValue, minValue)
        return minValue - series

    def _readLevelUpTotalValue(self, dossier):
        return RECORD_CONFIGS[self._name]

    def _readProgressValue(self, dossier):
        return 0