# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/battle_ability_slot_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_slot_model import BaseSlotModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.battle_ability_by_rank_model import BattleAbilityByRankModel

class BattleAbilitySlotModel(BaseSlotModel):
    __slots__ = ()

    def __init__(self, properties=26, commands=0):
        super(BattleAbilitySlotModel, self).__init__(properties=properties, commands=commands)

    def getLevel(self):
        return self._getNumber(20)

    def setLevel(self, value):
        self._setNumber(20, value)

    def getKeyName(self):
        return self._getString(21)

    def setKeyName(self, value):
        self._setString(21, value)

    def getDescription(self):
        return self._getString(22)

    def setDescription(self, value):
        self._setString(22, value)

    def getCategory(self):
        return self._getString(23)

    def setCategory(self, value):
        self._setString(23, value)

    def getRanks(self):
        return self._getArray(24)

    def setRanks(self, value):
        self._setArray(24, value)

    @staticmethod
    def getRanksType():
        return unicode

    def getAbilitiesByRank(self):
        return self._getArray(25)

    def setAbilitiesByRank(self, value):
        self._setArray(25, value)

    @staticmethod
    def getAbilitiesByRankType():
        return BattleAbilityByRankModel

    def _initialize(self):
        super(BattleAbilitySlotModel, self)._initialize()
        self._addNumberProperty('level', 0)
        self._addStringProperty('keyName', '')
        self._addStringProperty('description', '')
        self._addStringProperty('category', '')
        self._addArrayProperty('ranks', Array())
        self._addArrayProperty('abilitiesByRank', Array())