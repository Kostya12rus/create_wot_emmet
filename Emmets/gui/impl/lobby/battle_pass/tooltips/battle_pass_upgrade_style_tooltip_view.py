# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/battle_pass/tooltips/battle_pass_upgrade_style_tooltip_view.py
from frameworks.wulf import ViewSettings
from gui.Scaleform.daapi.view.lobby.customization.shared import getSuitableText
from gui.battle_pass.battle_pass_helpers import getStyleForChapter
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.battle_pass_upgrade_style_tooltip_view_model import BattlePassUpgradeStyleTooltipViewModel
from gui.impl.pub import ViewImpl

class BattlePassUpgradeStyleTooltipView(ViewImpl):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.lobby.battle_pass.tooltips.BattlePassUpgradeStyleTooltipView())
        settings.model = BattlePassUpgradeStyleTooltipViewModel()
        settings.args = args
        settings.kwargs = kwargs
        super(BattlePassUpgradeStyleTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(BattlePassUpgradeStyleTooltipView, self).getViewModel()

    def _onLoading(self, chapter, level, *args, **kwargs):
        customizationItem = getStyleForChapter(chapter)
        with self.viewModel.transaction() as (model):
            if customizationItem is not None:
                model.setStyleId(customizationItem.id)
                model.setStyleName(customizationItem.userName)
                model.setVehicles(getSuitableText(customizationItem, formatVehicle=False))
            else:
                model.setStyleId(0)
                model.setStyleName('')
                model.setVehicles('')
            model.setLevel(level)
        return