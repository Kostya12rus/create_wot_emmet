# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/battle_pass/tooltips/battle_pass_completed_tooltip_view.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.battle_pass_completed_tooltip_view_model import BattlePassCompletedTooltipViewModel
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.game_control import IBattlePassController

class BattlePassCompletedTooltipView(ViewImpl):
    __battlePassController = dependency.descriptor(IBattlePassController)
    __slots__ = ()

    def __init__(self):
        settings = ViewSettings(R.views.lobby.battle_pass.tooltips.BattlePassCompletedTooltipView())
        settings.model = BattlePassCompletedTooltipViewModel()
        super(BattlePassCompletedTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(BattlePassCompletedTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(BattlePassCompletedTooltipView, self)._onLoading(*args, **kwargs)
        bpController = self.__battlePassController
        isBought = all(bpController.isBought(chapterID=chapter) for chapter in bpController.getChapterIDs())
        with self.getViewModel().transaction() as (model):
            model.setIsBattlePassPurchased(isBought)
            model.setNotChosenRewardCount(self.__battlePassController.getNotChosenRewardCount())