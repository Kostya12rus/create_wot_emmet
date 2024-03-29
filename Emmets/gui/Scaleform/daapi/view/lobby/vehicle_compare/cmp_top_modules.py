# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/cmp_top_modules.py
import operator
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.items_parameters import params
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.shared import IItemsCache
_COMMON_CRITERIA = REQ_CRITERIA.EMPTY | ~REQ_CRITERIA.HIDDEN

class _BaseModuleComparator(object):
    itemsCache = dependency.descriptor(IItemsCache)
    __slots__ = ('_items', '_vehicle')

    def __init__(self, items, vehicle):
        super(_BaseModuleComparator, self).__init__()
        self._items = items
        self._vehicle = vehicle

    def clear(self):
        self._items = None
        return

    def maxLvl(self, excludes=None):

        def __key(item):
            return item.level

        return self._getModuleParam(__key, excludes)

    def maxCreditsCost(self, excludes=None):

        def __key(item):
            return item.buyPrices.itemPrice.price[0]

        return self._getModuleParam(__key, excludes)

    def mostValuableParam(self, excludes=None):
        pass

    def _getModuleParam(self, getter, excludes=None):
        items = [ x for x in self._items.values() if x not in excludes ]
        if not items:
            return (False, None)
        else:
            if len(items) == 1:
                return (True, self._items.values()[0])
            sortedItems = sorted(items, key=getter)
            if getter(sortedItems[-1]) == getter(sortedItems[-2]):
                return (False, sortedItems[-1])
            return (True, sortedItems[-1])

    def _getValuableParam(self, paramName, excludes=None):
        res = []
        getter = operator.attrgetter(paramName)
        for _, module in self._items.items():
            if excludes and module in excludes:
                continue
            maxLoad = getter(module.descriptor)
            res.append((maxLoad, module))

        if not res:
            return (False, None)
        else:
            res = sorted(res)
            return (True, res[-1][1])


class TopModulesChecker(object):
    __slots__ = ('_comparators', '_requestCriteria', '__vehicle')

    def __init__(self, vehicle):
        super(TopModulesChecker, self).__init__()
        self.__vehicle = vehicle
        self._requestCriteria = _COMMON_CRITERIA | REQ_CRITERIA.VEHICLE.SUITABLE([self.__vehicle])
        self._comparators = [
         ChassisComparator(self._requestCriteria, self.__vehicle),
         TurretComparator(self._requestCriteria, self.__vehicle),
         GunComparator(self._requestCriteria, self.__vehicle),
         EngineComparator(self._requestCriteria, self.__vehicle),
         RadioComparator(self._requestCriteria, self.__vehicle)]

    def process(self):
        modules = []
        for comparator in self._comparators:
            for functor in (comparator.maxLvl, comparator.maxCreditsCost, comparator.mostValuableParam):
                fit, module = self.__check(functor)
                if fit:
                    modules.append(module)
                    break

        return modules

    def clear(self):
        for comparator in self._comparators:
            comparator.clear()

    def __check(self, functor):
        excludes = []
        while True:
            found, module = functor(excludes)
            if found:
                if module.mayInstall(self.__vehicle):
                    return (True, module)
                excludes.append(module)
            else:
                return (
                 False, None)

        return


class ChassisComparator(_BaseModuleComparator):

    def __init__(self, criteria, vehicle):
        items = self.itemsCache.items.getItems(GUI_ITEM_TYPE.CHASSIS, criteria)
        super(ChassisComparator, self).__init__(items, vehicle)

    def mostValuableParam(self, excludes=None):
        return self._getValuableParam('maxLoad', excludes)


class TurretComparator(_BaseModuleComparator):

    def __init__(self, criteria, vehicle):
        items = self.itemsCache.items.getItems(GUI_ITEM_TYPE.TURRET, criteria)
        super(TurretComparator, self).__init__(items, vehicle)

    def mostValuableParam(self, excludes=None):
        return self._getValuableParam('primaryArmor', excludes)


class GunComparator(_BaseModuleComparator):
    __slots__ = ('__vehicle', )

    def __init__(self, criteria, vehicle):
        items = self.itemsCache.items.getItems(GUI_ITEM_TYPE.GUN, criteria)
        super(GunComparator, self).__init__(items, vehicle)

    def mostValuableParam(self, excludes=None):
        res = []
        for _, module in self._items.items():
            if excludes and module in excludes:
                continue
            gp = params.GunParams(module.descriptor, self._vehicle.descriptor)
            if gp:
                paramsDict = gp.getParamsDict()
                avgDamage = paramsDict.get('avgDamagePerMinute', 0.0)
                res.append((avgDamage, module))

        if not res:
            return (False, None)
        else:
            res = sorted(res)
            return (True, res[-1][1])


class EngineComparator(_BaseModuleComparator):

    def __init__(self, criteria, vehicle):
        items = self.itemsCache.items.getItems(GUI_ITEM_TYPE.ENGINE, criteria)
        super(EngineComparator, self).__init__(items, vehicle)

    def mostValuableParam(self, excludes=None):
        return self._getValuableParam('power', excludes=excludes)


class RadioComparator(_BaseModuleComparator):

    def __init__(self, criteria, vehicle):
        items = self.itemsCache.items.getItems(GUI_ITEM_TYPE.RADIO, criteria)
        super(RadioComparator, self).__init__(items, vehicle)

    def mostValuableParam(self, excludes=None):
        return self._getValuableParam('distance', excludes=excludes)