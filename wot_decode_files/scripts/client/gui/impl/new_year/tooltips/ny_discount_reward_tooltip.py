# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/new_year/tooltips/ny_discount_reward_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from gui.impl.gen.view_models.views.lobby.new_year.tooltips.ny_discount_reward_tooltip_model import NyDiscountRewardTooltipModel
from new_year.variadic_discount import VariadicDiscount

class NyDiscountRewardTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.lobby.new_year.tooltips.NyDiscountRewardTooltip())
        settings.model = NyDiscountRewardTooltipModel()
        settings.args = args
        settings.kwargs = kwargs
        super(NyDiscountRewardTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(NyDiscountRewardTooltip, self).getViewModel()

    def _initialize(self, variadicID, discount):
        variadicDiscount = VariadicDiscount(variadicID)
        with self.viewModel.transaction() as (tx):
            tx.setLevel(variadicDiscount.getTankLevel())
            tx.setDiscount(discount)
            selectedVehicle = variadicDiscount.getSelectedVehicle()
            if selectedVehicle:
                tx.setSelectedVehicle(selectedVehicle.userName)