# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/cn_loot_boxes/tooltips/infotype_slot_model.py
from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.cn_loot_boxes.tooltips.infotype_reward_model import InfotypeRewardModel

class RewardType(Enum):
    VEHICLE = 'vehicle'
    DEFAULT = 'default'


class InfotypeSlotModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(InfotypeSlotModel, self).__init__(properties=properties, commands=commands)

    def getProbability(self):
        return self._getReal(0)

    def setProbability(self, value):
        self._setReal(0, value)

    def getRewardType(self):
        return RewardType(self._getString(1))

    def setRewardType(self, value):
        self._setString(1, value.value)

    def getRewards(self):
        return self._getArray(2)

    def setRewards(self, value):
        self._setArray(2, value)

    @staticmethod
    def getRewardsType():
        return InfotypeRewardModel

    def _initialize(self):
        super(InfotypeSlotModel, self)._initialize()
        self._addRealProperty('probability', 0.0)
        self._addStringProperty('rewardType')
        self._addArrayProperty('rewards', Array())