# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/customization/customization_cart/cart_tutorial_model.py
from frameworks.wulf import ViewModel

class CartTutorialModel(ViewModel):
    __slots__ = ('onTutorialClose', )

    def __init__(self, properties=1, commands=1):
        super(CartTutorialModel, self).__init__(properties=properties, commands=commands)

    def getShowProlongHint(self):
        return self._getBool(0)

    def setShowProlongHint(self, value):
        self._setBool(0, value)

    def _initialize(self):
        super(CartTutorialModel, self)._initialize()
        self._addBoolProperty('showProlongHint', False)
        self.onTutorialClose = self._addCommand('onTutorialClose')