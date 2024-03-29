# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/exchange_panel_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.exchange_rate_model import ExchangeRateModel
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel

class ExchangePanelModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ExchangePanelModel, self).__init__(properties=properties, commands=commands)

    @property
    def fromItem(self):
        return self._getViewModel(0)

    @staticmethod
    def getFromItemType():
        return PriceItemModel

    @property
    def toItem(self):
        return self._getViewModel(1)

    @staticmethod
    def getToItemType():
        return PriceItemModel

    @property
    def exchangeRate(self):
        return self._getViewModel(2)

    @staticmethod
    def getExchangeRateType():
        return ExchangeRateModel

    def _initialize(self):
        super(ExchangePanelModel, self)._initialize()
        self._addViewModelProperty('fromItem', PriceItemModel())
        self._addViewModelProperty('toItem', PriceItemModel())
        self._addViewModelProperty('exchangeRate', ExchangeRateModel())