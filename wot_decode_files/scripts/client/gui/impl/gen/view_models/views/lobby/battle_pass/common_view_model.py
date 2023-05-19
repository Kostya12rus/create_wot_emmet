# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/common_view_model.py
from frameworks.wulf import ViewModel

class CommonViewModel(ViewModel):
    __slots__ = ('onClosed', )

    def __init__(self, properties=4, commands=1):
        super(CommonViewModel, self).__init__(properties=properties, commands=commands)

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)

    def getCurrentLevel(self):
        return self._getNumber(1)

    def setCurrentLevel(self, value):
        self._setNumber(1, value)

    def getIsBattlePassPurchased(self):
        return self._getBool(2)

    def setIsBattlePassPurchased(self, value):
        self._setBool(2, value)

    def getCanBuy(self):
        return self._getBool(3)

    def setCanBuy(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(CommonViewModel, self)._initialize()
        self._addStringProperty('title', '')
        self._addNumberProperty('currentLevel', 0)
        self._addBoolProperty('isBattlePassPurchased', False)
        self._addBoolProperty('canBuy', False)
        self.onClosed = self._addCommand('onClosed')