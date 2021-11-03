# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/abstract/series.py
from regular import RegularAchievement
from gui.impl import backport

class SeriesAchievement(RegularAchievement):
    __slots__ = ()

    def getMaxSeriesInfo(self):
        return (
         self._getCounterRecordNames()[1], self.getValue())

    def getI18nValue(self):
        return backport.getIntegralFormat(self._value)

    def _getCounterRecordNames(self):
        return (None, None)

    def _readValue(self, dossier):
        record = self._getCounterRecordNames()[1]
        if record is not None:
            return dossier.getRecordValue(*record)
        else:
            return 0

    def _readLevelUpTotalValue(self, dossier):
        return self._value + 1

    def _readLevelUpValue(self, dossier):
        record = self._getCounterRecordNames()[0]
        if record is not None:
            return self._lvlUpTotalValue - dossier.getRecordValue(*record)
        else:
            return 0