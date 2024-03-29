# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/dialogs/sub_views/single_price_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.dialogs.dialog_template_generic_tooltip_view_model import DialogTemplateGenericTooltipViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencyViewModel

class SinglePriceViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(SinglePriceViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def cost(self):
        return self._getViewModel(0)

    @staticmethod
    def getCostType():
        return CurrencyViewModel

    @property
    def tooltip(self):
        return self._getViewModel(1)

    @staticmethod
    def getTooltipType():
        return DialogTemplateGenericTooltipViewModel

    def getText(self):
        return self._getString(2)

    def setText(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(SinglePriceViewModel, self)._initialize()
        self._addViewModelProperty('cost', CurrencyViewModel())
        self._addViewModelProperty('tooltip', DialogTemplateGenericTooltipViewModel())
        self._addStringProperty('text', '')