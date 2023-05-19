# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/missions/quest_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel
from gui.impl.gen.view_models.common.missions.conditions.condition_group_model import ConditionGroupModel
from gui.impl.gen.view_models.common.missions.event_model import EventModel

class QuestModel(EventModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(QuestModel, self).__init__(properties=properties, commands=commands)

    @property
    def preBattleCondition(self):
        return self._getViewModel(7)

    @staticmethod
    def getPreBattleConditionType():
        return ConditionGroupModel

    @property
    def bonusCondition(self):
        return self._getViewModel(8)

    @staticmethod
    def getBonusConditionType():
        return ConditionGroupModel

    @property
    def postBattleCondition(self):
        return self._getViewModel(9)

    @staticmethod
    def getPostBattleConditionType():
        return ConditionGroupModel

    def getBonuses(self):
        return self._getArray(10)

    def setBonuses(self, value):
        self._setArray(10, value)

    @staticmethod
    def getBonusesType():
        return BonusModel

    def _initialize(self):
        super(QuestModel, self)._initialize()
        self._addViewModelProperty('preBattleCondition', ConditionGroupModel())
        self._addViewModelProperty('bonusCondition', ConditionGroupModel())
        self._addViewModelProperty('postBattleCondition', ConditionGroupModel())
        self._addArrayProperty('bonuses', Array())