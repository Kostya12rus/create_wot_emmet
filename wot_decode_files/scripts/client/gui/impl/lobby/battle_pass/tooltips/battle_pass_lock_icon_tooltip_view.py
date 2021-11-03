# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/battle_pass/tooltips/battle_pass_lock_icon_tooltip_view.py
from frameworks.wulf import ViewModel, ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class BattlePassLockIconTooltipView(ViewImpl):
    __slots__ = ()

    def __init__(self):
        settings = ViewSettings(R.views.lobby.battle_pass.tooltips.BattlePassLockIconTooltipView())
        settings.model = ViewModel()
        super(BattlePassLockIconTooltipView, self).__init__(settings)