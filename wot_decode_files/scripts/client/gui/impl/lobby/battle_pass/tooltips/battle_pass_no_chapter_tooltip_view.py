# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/battle_pass/tooltips/battle_pass_no_chapter_tooltip_view.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.battle_pass_no_chapter_tooltip_view_model import BattlePassNoChapterTooltipViewModel
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.game_control import IBattlePassController

class BattlePassNoChapterTooltipView(ViewImpl):
    __battlePassController = dependency.descriptor(IBattlePassController)
    __slots__ = ()

    def __init__(self):
        settings = ViewSettings(R.views.lobby.battle_pass.tooltips.BattlePassNoChapterTooltipView())
        settings.model = BattlePassNoChapterTooltipViewModel()
        super(BattlePassNoChapterTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(BattlePassNoChapterTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(BattlePassNoChapterTooltipView, self)._onLoading(*args, **kwargs)
        with self.getViewModel().transaction() as (model):
            model.setPoints(self.__battlePassController.getFreePoints())