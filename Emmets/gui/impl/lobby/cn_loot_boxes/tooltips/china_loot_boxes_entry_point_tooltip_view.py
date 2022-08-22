# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/cn_loot_boxes/tooltips/china_loot_boxes_entry_point_tooltip_view.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.cn_loot_boxes.tooltips.entry_point_model import EntryPointModel
from gui.impl.pub import ViewImpl

class ChinaLootBoxesEntryPointTooltipView(ViewImpl):
    __slots__ = ()

    def __init__(self):
        settings = ViewSettings(R.views.lobby.cn_loot_boxes.tooltips.ChinaLootBoxesEntryPointTooltipView())
        settings.model = EntryPointModel()
        super(ChinaLootBoxesEntryPointTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(ChinaLootBoxesEntryPointTooltipView, self).getViewModel()