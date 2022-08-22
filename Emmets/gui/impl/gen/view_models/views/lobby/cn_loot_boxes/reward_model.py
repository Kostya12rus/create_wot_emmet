# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/cn_loot_boxes/reward_model.py
from enum import Enum
from gui.impl.gen import R
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class RewardType(Enum):
    VEHICLE = 'vehicle'
    DEFAULT = 'default'


class RewardModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(RewardModel, self).__init__(properties=properties, commands=commands)

    def getIconSource(self):
        return self._getResource(8)

    def setIconSource(self, value):
        self._setResource(8, value)

    def getCount(self):
        return self._getNumber(9)

    def setCount(self, value):
        self._setNumber(9, value)

    def _initialize(self):
        super(RewardModel, self)._initialize()
        self._addResourceProperty('iconSource', R.invalid())
        self._addNumberProperty('count', 0)