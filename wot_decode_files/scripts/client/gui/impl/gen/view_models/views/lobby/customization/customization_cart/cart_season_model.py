# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/customization/customization_cart/cart_season_model.py
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.customization.customization_cart.cart_slot_model import CartSlotModel

class CartSeasonModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(CartSeasonModel, self).__init__(properties=properties, commands=commands)

    @property
    def items(self):
        return self._getViewModel(0)

    @staticmethod
    def getItemsType():
        return CartSlotModel

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)

    def getCount(self):
        return self._getNumber(2)

    def setCount(self, value):
        self._setNumber(2, value)

    def getBonusType(self):
        return self._getString(3)

    def setBonusType(self, value):
        self._setString(3, value)

    def getBonusValue(self):
        return self._getString(4)

    def setBonusValue(self, value):
        self._setString(4, value)

    def _initialize(self):
        super(CartSeasonModel, self)._initialize()
        self._addViewModelProperty('items', UserListModel())
        self._addStringProperty('name', '')
        self._addNumberProperty('count', -1)
        self._addStringProperty('bonusType', '')
        self._addStringProperty('bonusValue', '')