# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/dialogs/sub_views/select_money_view_model.py
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencyViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.select_option_base_item_view_model import SelectOptionBaseItemViewModel

class SelectMoneyViewModel(SelectOptionBaseItemViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(SelectMoneyViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def cost(self):
        return self._getViewModel(4)

    @staticmethod
    def getCostType():
        return CurrencyViewModel

    def _initialize(self):
        super(SelectMoneyViewModel, self)._initialize()
        self._addViewModelProperty('cost', CurrencyViewModel())