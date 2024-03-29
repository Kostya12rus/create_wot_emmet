# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/common/buy_sell_items_dialog_model.py
from gui.impl.gen import R
from gui.impl.gen.view_models.windows.full_screen_dialog_window_model import FullScreenDialogWindowModel

class BuySellItemsDialogModel(FullScreenDialogWindowModel):
    __slots__ = ()

    def __init__(self, properties=24, commands=3):
        super(BuySellItemsDialogModel, self).__init__(properties=properties, commands=commands)

    def getBackgroundImg(self):
        return self._getResource(11)

    def setBackgroundImg(self, value):
        self._setResource(11, value)

    def getDescription(self):
        return self._getResource(12)

    def setDescription(self, value):
        self._setResource(12, value)

    def getUpperDescription(self):
        return self._getResource(13)

    def setUpperDescription(self, value):
        self._setResource(13, value)

    def getLowerDescription(self):
        return self._getResource(14)

    def setLowerDescription(self, value):
        self._setResource(14, value)

    def getIsAlert(self):
        return self._getBool(15)

    def setIsAlert(self, value):
        self._setBool(15, value)

    def getCurrencyType(self):
        return self._getString(16)

    def setCurrencyType(self, value):
        self._setString(16, value)

    def getItemPrice(self):
        return self._getNumber(17)

    def setItemPrice(self, value):
        self._setNumber(17, value)

    def getItemCount(self):
        return self._getNumber(18)

    def setItemCount(self, value):
        self._setNumber(18, value)

    def getItemMaxCount(self):
        return self._getNumber(19)

    def setItemMaxCount(self, value):
        self._setNumber(19, value)

    def getItemMinCount(self):
        return self._getNumber(20)

    def setItemMinCount(self, value):
        self._setNumber(20, value)

    def getItemTotalPrice(self):
        return self._getNumber(21)

    def setItemTotalPrice(self, value):
        self._setNumber(21, value)

    def getTooltipMsg(self):
        return self._getString(22)

    def setTooltipMsg(self, value):
        self._setString(22, value)

    def getSpecialType(self):
        return self._getString(23)

    def setSpecialType(self, value):
        self._setString(23, value)

    def _initialize(self):
        super(BuySellItemsDialogModel, self)._initialize()
        self._addResourceProperty('backgroundImg', R.invalid())
        self._addResourceProperty('description', R.invalid())
        self._addResourceProperty('upperDescription', R.invalid())
        self._addResourceProperty('lowerDescription', R.invalid())
        self._addBoolProperty('isAlert', False)
        self._addStringProperty('currencyType', '')
        self._addNumberProperty('itemPrice', 0)
        self._addNumberProperty('itemCount', 1)
        self._addNumberProperty('itemMaxCount', 1)
        self._addNumberProperty('itemMinCount', 1)
        self._addNumberProperty('itemTotalPrice', 0)
        self._addStringProperty('tooltipMsg', '')
        self._addStringProperty('specialType', '')