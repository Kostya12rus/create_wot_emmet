# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/compound_price_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.price_model import PriceModel

class CompoundPriceModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(CompoundPriceModel, self).__init__(properties=properties, commands=commands)

    def getPrices(self):
        return self._getArray(0)

    def setPrices(self, value):
        self._setArray(0, value)

    @staticmethod
    def getPricesType():
        return PriceModel

    def _initialize(self):
        super(CompoundPriceModel, self)._initialize()
        self._addArrayProperty('prices', Array())