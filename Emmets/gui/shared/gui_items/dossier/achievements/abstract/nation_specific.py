# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/abstract/nation_specific.py
from simple_progress import SimpleProgressAchievement
from dossiers2.custom import cache
from dossiers2.custom.cache import getCache as getDossiersCache
from gui import nationCompareByIndex

class NationSpecificAchievement(SimpleProgressAchievement):
    __slots__ = ('_nationID', )
    _NATIONAL_VEHICLES = 'vehiclesInTreesByNation'
    _LIST_NAME = ''

    def __init__(self, namePrefix, nationID, block, dossier, value=None):
        self._nationID = nationID
        super(NationSpecificAchievement, self).__init__(self.makeFullName(namePrefix, nationID), block, dossier, value)

    def getNationID(self):
        return self._nationID

    @classmethod
    def getVehiclesListTitle(cls):
        return cls._LIST_NAME

    @classmethod
    def makeFullName(cls, name, nationID):
        if nationID != -1:
            name += str(nationID)
        return name

    def _readValue(self, dossier):
        return 0

    def _readLevelUpTotalValue(self, dossier):
        dossierCache = cache.getCache()
        if self._nationID != -1:
            return len(dossierCache[self._NATIONAL_VEHICLES].get(self._nationID, []))
        else:
            return len(self._getAllSuitableVehicles())

    @classmethod
    def _getAllSuitableVehicles(cls):
        return getDossiersCache()['vehiclesInTrees']

    def _getDoneStatus(self, dossier):
        return bool(dossier.getRecordValue(*self.getRecordName()))

    def __cmp__(self, other):
        res = super(NationSpecificAchievement, self).__cmp__(other)
        if res:
            return res
        if isinstance(other, NationSpecificAchievement):
            if self._nationID != -1 and other._nationID != -1:
                return nationCompareByIndex(self._nationID, other._nationID)
        return 0