# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/battle_pass/tooltips/battle_pass_coin_tooltip_view.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.battle_pass_coin_tooltip_view_model import BattlePassCoinTooltipViewModel
from gui.impl.pub import ViewImpl

class BattlePassCoinTooltipView(ViewImpl):
    __slots__ = ()

    def __init__(self):
        settings = ViewSettings(R.views.lobby.battle_pass.tooltips.BattlePassCoinTooltipView())
        settings.model = BattlePassCoinTooltipViewModel()
        super(BattlePassCoinTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(BattlePassCoinTooltipView, self).getViewModel()