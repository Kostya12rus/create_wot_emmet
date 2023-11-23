# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/crew_book_reward_option_model.py
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_option_model import RewardOptionModel

class CrewBookRewardOptionModel(RewardOptionModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(CrewBookRewardOptionModel, self).__init__(properties=properties, commands=commands)

    def getExpBonusValue(self):
        return self._getNumber(6)

    def setExpBonusValue(self, value):
        self._setNumber(6, value)

    def _initialize(self):
        super(CrewBookRewardOptionModel, self)._initialize()
        self._addNumberProperty('expBonusValue', 0)