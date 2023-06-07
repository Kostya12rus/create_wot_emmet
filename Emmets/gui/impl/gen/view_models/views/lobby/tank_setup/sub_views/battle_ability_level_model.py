# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/battle_ability_level_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.battle_ability_level_param_model import BattleAbilityLevelParamModel

class BattleAbilityLevelModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BattleAbilityLevelModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)

    def getParams(self):
        return self._getArray(1)

    def setParams(self, value):
        self._setArray(1, value)

    @staticmethod
    def getParamsType():
        return BattleAbilityLevelParamModel

    def _initialize(self):
        super(BattleAbilityLevelModel, self)._initialize()
        self._addNumberProperty('id', 0)
        self._addArrayProperty('params', Array())