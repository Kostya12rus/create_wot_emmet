# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/mapbox/crew_book_reward_option_model.py
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class CrewBookRewardOptionModel(BonusModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(CrewBookRewardOptionModel, self).__init__(properties=properties, commands=commands)

    def getExpBonusValue(self):
        return self._getNumber(7)

    def setExpBonusValue(self, value):
        self._setNumber(7, value)

    def getIcon(self):
        return self._getString(8)

    def setIcon(self, value):
        self._setString(8, value)

    def getDescription(self):
        return self._getString(9)

    def setDescription(self, value):
        self._setString(9, value)

    def getItemID(self):
        return self._getNumber(10)

    def setItemID(self, value):
        self._setNumber(10, value)

    def _initialize(self):
        super(CrewBookRewardOptionModel, self)._initialize()
        self._addNumberProperty('expBonusValue', 0)
        self._addStringProperty('icon', '')
        self._addStringProperty('description', '')
        self._addNumberProperty('itemID', 0)