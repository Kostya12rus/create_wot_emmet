# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/battle_matters/tooltips/battle_matters_token_tooltip_view.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.battle_matters.tooltips.battle_matters_token_tooltip_view_model import BattleMattersTokenTooltipViewModel
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.battle_matters import IBattleMattersController
from skeletons.gui.shared import IItemsCache

class BattleMattersTokenTooltipView(ViewImpl):
    __slots__ = ()
    __battleMattersController = dependency.descriptor(IBattleMattersController)
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self):
        settings = ViewSettings(R.views.lobby.battle_matters.tooltips.BattleMattersTokenTooltipView())
        settings.model = BattleMattersTokenTooltipViewModel()
        super(BattleMattersTokenTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(BattleMattersTokenTooltipView, self).getViewModel()

    def _onLoading(self):
        super(BattleMattersTokenTooltipView, self)._onLoading()
        if self.__battleMattersController.isFinished():
            self.viewModel.setEndDate(self.__itemsCache.items.tokens.getTokenInfo(self.__battleMattersController.getDelayedRewardCurrencyToken())[0])