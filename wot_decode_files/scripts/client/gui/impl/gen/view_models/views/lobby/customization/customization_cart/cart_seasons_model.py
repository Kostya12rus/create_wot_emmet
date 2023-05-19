# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/customization/customization_cart/cart_seasons_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.customization.customization_cart.cart_season_model import CartSeasonModel

class CartSeasonsModel(ViewModel):
    __slots__ = ('onSelectItem', )

    def __init__(self, properties=3, commands=1):
        super(CartSeasonsModel, self).__init__(properties=properties, commands=commands)

    @property
    def winter(self):
        return self._getViewModel(0)

    @staticmethod
    def getWinterType():
        return CartSeasonModel

    @property
    def summer(self):
        return self._getViewModel(1)

    @staticmethod
    def getSummerType():
        return CartSeasonModel

    @property
    def desert(self):
        return self._getViewModel(2)

    @staticmethod
    def getDesertType():
        return CartSeasonModel

    def _initialize(self):
        super(CartSeasonsModel, self)._initialize()
        self._addViewModelProperty('winter', CartSeasonModel())
        self._addViewModelProperty('summer', CartSeasonModel())
        self._addViewModelProperty('desert', CartSeasonModel())
        self.onSelectItem = self._addCommand('onSelectItem')