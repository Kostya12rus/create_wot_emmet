# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/collection/reward_model.py
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class RewardModel(ItemBonusModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(RewardModel, self).__init__(properties=properties, commands=commands)

    def getItem(self):
        return self._getString(9)

    def setItem(self, value):
        self._setString(9, value)

    def getIcon(self):
        return self._getString(10)

    def setIcon(self, value):
        self._setString(10, value)

    def getUserName(self):
        return self._getString(11)

    def setUserName(self, value):
        self._setString(11, value)

    def _initialize(self):
        super(RewardModel, self)._initialize()
        self._addStringProperty('item', '')
        self._addStringProperty('icon', '')
        self._addStringProperty('userName', '')