# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/customization/customization_cart/cart_style_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class CartStyleModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(CartStyleModel, self).__init__(properties=properties, commands=commands)

    def getIsStyle(self):
        return self._getBool(0)

    def setIsStyle(self, value):
        self._setBool(0, value)

    def getStyleTypeName(self):
        return self._getResource(1)

    def setStyleTypeName(self, value):
        self._setResource(1, value)

    def getStyleName(self):
        return self._getString(2)

    def setStyleName(self, value):
        self._setString(2, value)

    def getIsEditable(self):
        return self._getBool(3)

    def setIsEditable(self, value):
        self._setBool(3, value)

    def getIsProlongStyleRent(self):
        return self._getBool(4)

    def setIsProlongStyleRent(self, value):
        self._setBool(4, value)

    def _initialize(self):
        super(CartStyleModel, self)._initialize()
        self._addBoolProperty('isStyle', False)
        self._addResourceProperty('styleTypeName', R.invalid())
        self._addStringProperty('styleName', '')
        self._addBoolProperty('isEditable', False)
        self._addBoolProperty('isProlongStyleRent', False)