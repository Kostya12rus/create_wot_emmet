# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/new_year/tooltips/ny_tank_extra_slot_tooltip.py
from frameworks.wulf import View, ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.tooltips.ny_tank_extra_slot_tooltip_model import NyTankExtraSlotTooltipModel
from gui.impl.lobby.new_year.ny_views_helpers import setSlotTooltipBonuses

class NYTankExtraSlotTooltipContent(View):

    def __init__(self):
        settings = ViewSettings(R.views.lobby.new_year.tooltips.ny_tank_extra_slot_tooltip.NYTankExtraSlotTooltipContent())
        settings.model = NyTankExtraSlotTooltipModel()
        super(NYTankExtraSlotTooltipContent, self).__init__(settings)

    @property
    def viewModel(self):
        return super(NYTankExtraSlotTooltipContent, self).getViewModel()

    def _initialize(self):
        super(NYTankExtraSlotTooltipContent, self)._initialize()
        with self.viewModel.transaction() as (vm):
            setSlotTooltipBonuses(vm)