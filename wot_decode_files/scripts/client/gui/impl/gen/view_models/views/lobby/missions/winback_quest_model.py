# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/missions/winback_quest_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class WinbackQuestModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(WinbackQuestModel, self).__init__(properties=properties, commands=commands)

    def getQuestNumber(self):
        return self._getNumber(0)

    def setQuestNumber(self, value):
        self._setNumber(0, value)

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def _initialize(self):
        super(WinbackQuestModel, self)._initialize()
        self._addNumberProperty('questNumber', 0)
        self._addArrayProperty('rewards', Array())