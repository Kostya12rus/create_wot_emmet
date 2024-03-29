# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/abstract/mixins/HasVehicleList.py
from collections import namedtuple
from gui import nationCompareByIndex
from helpers import dependency
from skeletons.gui.shared import IItemsCache

class HasVehiclesList(object):
    _LIST_NAME = 'vehicles'
    VehicleData = namedtuple('VehicleData', 'name nation level type icon')
    itemsCache = dependency.descriptor(IItemsCache)

    def getVehiclesData(self):
        result = []
        for vCD in self._getVehiclesDescrsList():
            vehicle = self.itemsCache.items.getItemByCD(vCD)
            result.append(self.VehicleData(vehicle.userName, vehicle.nationID, vehicle.level, vehicle.type, vehicle.iconSmall))

        return map((lambda i: i._asdict()), sorted(result, cmp=self.__sortFunc))

    @classmethod
    def getVehiclesListTitle(cls):
        return cls._LIST_NAME

    def _getVehiclesDescrsList(self):
        raise NotImplemented

    def hasVehiclesList(self):
        return True

    @classmethod
    def __sortFunc(cls, i1, i2):
        res = i1.level - i2.level
        if res:
            return res
        return nationCompareByIndex(i1.nation, i2.nation)