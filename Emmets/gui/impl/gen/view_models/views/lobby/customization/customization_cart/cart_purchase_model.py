# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/customization/customization_cart/cart_purchase_model.py
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_compound_price_model import UserCompoundPriceModel

class CartPurchaseModel(ViewModel):
    __slots__ = ('onBuyAction', )

    def __init__(self, properties=4, commands=1):
        super(CartPurchaseModel, self).__init__(properties=properties, commands=commands)

    @property
    def totalPrice(self):
        return self._getViewModel(0)

    @staticmethod
    def getTotalPriceType():
        return UserCompoundPriceModel

    def getPurchasedCount(self):
        return self._getNumber(1)

    def setPurchasedCount(self, value):
        self._setNumber(1, value)

    def getIsEnoughMoney(self):
        return self._getBool(2)

    def setIsEnoughMoney(self, value):
        self._setBool(2, value)

    def getIsGoldPrice(self):
        return self._getBool(3)

    def setIsGoldPrice(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(CartPurchaseModel, self)._initialize()
        self._addViewModelProperty('totalPrice', UserCompoundPriceModel())
        self._addNumberProperty('purchasedCount', 0)
        self._addBoolProperty('isEnoughMoney', False)
        self._addBoolProperty('isGoldPrice', False)
        self.onBuyAction = self._addCommand('onBuyAction')