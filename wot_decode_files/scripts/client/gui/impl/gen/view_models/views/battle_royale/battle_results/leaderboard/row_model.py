# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle_royale/battle_results/leaderboard/row_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.user_name_model import UserNameModel

class RowModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(RowModel, self).__init__(properties=properties, commands=commands)

    @property
    def user(self):
        return self._getViewModel(0)

    def getPlace(self):
        return self._getString(1)

    def setPlace(self, value):
        self._setString(1, value)

    def getType(self):
        return self._getString(2)

    def setType(self, value):
        self._setString(2, value)

    def getAnonymizerNick(self):
        return self._getString(3)

    def setAnonymizerNick(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(RowModel, self)._initialize()
        self._addViewModelProperty('user', UserNameModel())
        self._addStringProperty('place', '')
        self._addStringProperty('type', 'rowBrEnemy')
        self._addStringProperty('anonymizerNick', '')