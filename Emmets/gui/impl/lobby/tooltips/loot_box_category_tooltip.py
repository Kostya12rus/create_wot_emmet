# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tooltips/loot_box_category_tooltip.py
from gui.impl.pub import ViewImpl
from gui.impl.gen.view_models.views.loot_box_category_tooltip_model import LootBoxCategoryTooltipModel
from gui.impl.gen.resources import R
from frameworks.wulf import ViewSettings

class LootBoxCategoryTooltipContent(ViewImpl):
    __slots__ = ()

    def __init__(self, *args):
        settings = ViewSettings(R.views.lobby.tooltips.loot_box_category_tooltip.LootBoxCategoryTooltipContent())
        settings.model = LootBoxCategoryTooltipModel()
        settings.args = args
        super(LootBoxCategoryTooltipContent, self).__init__(settings)

    @property
    def viewModel(self):
        return super(LootBoxCategoryTooltipContent, self).getViewModel()

    def _initialize(self, category):
        super(LootBoxCategoryTooltipContent, self)._initialize()
        self.viewModel.setCategory(category)