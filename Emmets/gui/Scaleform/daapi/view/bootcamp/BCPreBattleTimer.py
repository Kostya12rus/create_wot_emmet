# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCPreBattleTimer.py
from gui.impl.gen import R
from gui.impl import backport
from gui.Scaleform.daapi.view.battle.shared.prebattle_timers.timer_base import PreBattleTimerBase

class BCPreBattleTimer(PreBattleTimerBase):

    def updateBattleCtx(self, battleCtx):
        self._battleTypeStr = battleCtx.getArenaWinString()
        self.as_setMessageS(self._getMessage())
        if self._isDisplayWinCondition():
            self.as_setWinConditionTextS(backport.text(R.strings.bootcamp.arena.name()))

    def _getMessage(self):
        return self._battleTypeStr