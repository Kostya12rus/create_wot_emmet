# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/instructions/booster_buy_model.py
from gui.impl.gen.view_models.views.lobby.common.buy_sell_items_dialog_model import BuySellItemsDialogModel

class BoosterBuyModel(BuySellItemsDialogModel):
    __slots__ = ('onSetIsRearm', )

    def __init__(self, properties=27, commands=4):
        super(BoosterBuyModel, self).__init__(properties=properties, commands=commands)

    def getIsRearm(self):
        return self._getBool(24)

    def setIsRearm(self, value):
        self._setBool(24, value)

    def getIsDiscount(self):
        return self._getBool(25)

    def setIsDiscount(self, value):
        self._setBool(25, value)

    def getDiscountValue(self):
        return self._getNumber(26)

    def setDiscountValue(self, value):
        self._setNumber(26, value)

    def _initialize(self):
        super(BoosterBuyModel, self)._initialize()
        self._addBoolProperty('isRearm', False)
        self._addBoolProperty('isDiscount', False)
        self._addNumberProperty('discountValue', 0)
        self.onSetIsRearm = self._addCommand('onSetIsRearm')