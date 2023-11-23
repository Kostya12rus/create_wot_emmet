# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/dialogs/sub_views/currency_with_tooltip_view_model.py
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencyViewModel

class CurrencyWithTooltipViewModel(CurrencyViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(CurrencyWithTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getDiscountTooltipContentId(self):
        return self._getNumber(7)

    def setDiscountTooltipContentId(self, value):
        self._setNumber(7, value)

    def _initialize(self):
        super(CurrencyWithTooltipViewModel, self)._initialize()
        self._addNumberProperty('discountTooltipContentId', 0)