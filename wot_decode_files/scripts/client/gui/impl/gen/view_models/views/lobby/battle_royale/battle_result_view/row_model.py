# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_royale/battle_result_view/row_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_royale.battle_result_view.user_battle_info_model import UserBattleInfoModel

class RowModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(RowModel, self).__init__(properties=properties, commands=commands)

    @property
    def user(self):
        return self._getViewModel(0)

    @staticmethod
    def getUserType():
        return UserBattleInfoModel

    def getType(self):
        return self._getString(1)

    def setType(self, value):
        self._setString(1, value)

    def getAnonymizerNick(self):
        return self._getString(2)

    def setAnonymizerNick(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(RowModel, self)._initialize()
        self._addViewModelProperty('user', UserBattleInfoModel())
        self._addStringProperty('type', 'rowBrEnemy')
        self._addStringProperty('anonymizerNick', '')