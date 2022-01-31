# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/new_year/popovers/ny_loot_box_statistics_reward_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class Type(Enum):
    NONE = ''
    VEHICLES = 'vehicles'
    CUSTOMIZATIONS = 'customizations'
    PREMIUMPLUS = 'premium_plus'
    GOLD = 'gold'
    CREDITS = 'credits'
    TOYS = 'ny22Toys'
    SHARDS = 'ny22ToyFragments'


class NyLootBoxStatisticsRewardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(NyLootBoxStatisticsRewardModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return Type(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)

    def getCount(self):
        return self._getNumber(1)

    def setCount(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(NyLootBoxStatisticsRewardModel, self)._initialize()
        self._addStringProperty('type')
        self._addNumberProperty('count', 0)