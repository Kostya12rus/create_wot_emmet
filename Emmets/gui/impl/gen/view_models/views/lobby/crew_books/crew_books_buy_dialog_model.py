# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew_books/crew_books_buy_dialog_model.py
from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel

class CrewBooksBuyDialogModel(ViewModel):
    __slots__ = ('onClosed', 'onStepperChanged', 'onBuyBtnClick')

    def __init__(self, properties=8, commands=3):
        super(CrewBooksBuyDialogModel, self).__init__(properties=properties, commands=commands)

    @property
    def bookPrice(self):
        return self._getViewModel(0)

    @staticmethod
    def getBookPriceType():
        return ListModel

    def getDialogTitle(self):
        return self._getString(1)

    def setDialogTitle(self, value):
        self._setString(1, value)

    def getBookIcon(self):
        return self._getResource(2)

    def setBookIcon(self, value):
        self._setResource(2, value)

    def getBookTitle(self):
        return self._getString(3)

    def setBookTitle(self, value):
        self._setString(3, value)

    def getBookDescription(self):
        return self._getResource(4)

    def setBookDescription(self, value):
        self._setResource(4, value)

    def getBookDescriptionFmtArgs(self):
        return self._getArray(5)

    def setBookDescriptionFmtArgs(self, value):
        self._setArray(5, value)

    def getBuyComplete(self):
        return self._getBool(6)

    def setBuyComplete(self, value):
        self._setBool(6, value)

    def getIsBuyEnable(self):
        return self._getBool(7)

    def setIsBuyEnable(self, value):
        self._setBool(7, value)

    def _initialize(self):
        super(CrewBooksBuyDialogModel, self)._initialize()
        self._addViewModelProperty('bookPrice', ListModel())
        self._addStringProperty('dialogTitle', '')
        self._addResourceProperty('bookIcon', R.invalid())
        self._addStringProperty('bookTitle', '')
        self._addResourceProperty('bookDescription', R.invalid())
        self._addArrayProperty('bookDescriptionFmtArgs', Array())
        self._addBoolProperty('buyComplete', False)
        self._addBoolProperty('isBuyEnable', False)
        self.onClosed = self._addCommand('onClosed')
        self.onStepperChanged = self._addCommand('onStepperChanged')
        self.onBuyBtnClick = self._addCommand('onBuyBtnClick')