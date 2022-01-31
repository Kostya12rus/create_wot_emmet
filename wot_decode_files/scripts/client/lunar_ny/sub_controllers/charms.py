# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/lunar_ny/sub_controllers/charms.py
import typing
from helpers import dependency
from lunar_ny.lunar_ny_charm import LunarNYCharm
from lunar_ny.sub_controllers import IBaseLunarSubController
from skeletons.gui.shared import IItemsCache

class CharmsSubController(IBaseLunarSubController):
    __itemsCache = dependency.descriptor(IItemsCache)

    def start(self):
        pass

    def stop(self):
        pass

    def getCharmBonuses(self):
        charms = self.getCharmsInSlots()
        bonuses = [ charm.getBonuses() for charm in charms if charm is not None ]
        return LunarNYCharm.computeSum(*bonuses)

    def getCharmsInSlots(self):
        return self.__itemsCache.items.lunarNY.getCharmsInSlots()

    def getCountCharms(self):
        return self.__itemsCache.items.lunarNY.getCountCharms()