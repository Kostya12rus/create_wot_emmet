# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/battle_pass_buy_confirm_view_model.py
from frameworks.wulf import ViewModel

class BattlePassBuyConfirmViewModel(ViewModel):
    __slots__ = ('onCloseClick', 'onBuyClick', 'onShowRewardsClick')

    def __init__(self, properties=3, commands=3):
        super(BattlePassBuyConfirmViewModel, self).__init__(properties=properties, commands=commands)

    def getPrice(self):
        return self._getNumber(0)

    def setPrice(self, value):
        self._setNumber(0, value)

    def getChapterID(self):
        return self._getNumber(1)

    def setChapterID(self, value):
        self._setNumber(1, value)

    def getIsActive(self):
        return self._getBool(2)

    def setIsActive(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(BattlePassBuyConfirmViewModel, self)._initialize()
        self._addNumberProperty('price', 0)
        self._addNumberProperty('chapterID', 0)
        self._addBoolProperty('isActive', False)
        self.onCloseClick = self._addCommand('onCloseClick')
        self.onBuyClick = self._addCommand('onBuyClick')
        self.onShowRewardsClick = self._addCommand('onShowRewardsClick')