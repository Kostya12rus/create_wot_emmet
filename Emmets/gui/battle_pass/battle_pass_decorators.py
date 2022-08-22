# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_pass/battle_pass_decorators.py
import typing
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.battle_pass.tooltips.battle_pass_coin_tooltip_view import BattlePassCoinTooltipView
from gui.impl.lobby.battle_pass.tooltips.battle_pass_lock_icon_tooltip_view import BattlePassLockIconTooltipView
from gui.impl.lobby.battle_pass.tooltips.battle_pass_points_view import BattlePassPointsTooltip
from gui.impl.lobby.battle_pass.tooltips.battle_pass_quests_chain_tooltip_view import BattlePassQuestsChainTooltipView
from gui.impl.lobby.battle_pass.tooltips.battle_pass_upgrade_style_tooltip_view import BattlePassUpgradeStyleTooltipView
if typing.TYPE_CHECKING:
    from gui.impl.backport import TooltipData

def createBackportTooltipDecorator():

    def decorator(func):

        def wrapper(self, event):
            if event.contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
                tooltipData = self.getTooltipData(event)
                if tooltipData is None:
                    return
                window = backport.BackportTooltipWindow(tooltipData, self.getParentWindow())
                if window is None:
                    return
                window.load()
                return window
            else:
                return func(self, event)

        return wrapper

    return decorator


def createTooltipContentDecorator():

    def decorator(func):

        def wrapper(self, event, contentID):
            tooltipData = self.getTooltipData(event)
            if contentID == R.views.lobby.battle_pass.tooltips.BattlePassUpgradeStyleTooltipView():
                if tooltipData is None:
                    return
                return BattlePassUpgradeStyleTooltipView(*tooltipData.specialArgs)
            else:
                if contentID == R.views.lobby.battle_pass.tooltips.BattlePassQuestsChainTooltipView():
                    if tooltipData is None:
                        return
                    return BattlePassQuestsChainTooltipView(*tooltipData.specialArgs)
                if contentID == R.views.lobby.battle_pass.tooltips.BattlePassCoinTooltipView():
                    return BattlePassCoinTooltipView()
                if contentID == R.views.lobby.battle_pass.tooltips.BattlePassPointsView():
                    return BattlePassPointsTooltip()
                if contentID == R.views.lobby.battle_pass.tooltips.BattlePassLockIconTooltipView():
                    return BattlePassLockIconTooltipView()
                return func(self, event, contentID)

        return wrapper

    return decorator