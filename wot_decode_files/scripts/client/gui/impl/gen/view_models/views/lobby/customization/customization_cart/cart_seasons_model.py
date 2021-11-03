# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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

    @property
    def summer(self):
        return self._getViewModel(1)

    @property
    def desert(self):
        return self._getViewModel(2)

    def _initialize(self):
        super(CartSeasonsModel, self)._initialize()
        self._addViewModelProperty('winter', CartSeasonModel())
        self._addViewModelProperty('summer', CartSeasonModel())
        self._addViewModelProperty('desert', CartSeasonModel())
        self.onSelectItem = self._addCommand('onSelectItem')