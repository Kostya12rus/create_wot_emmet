# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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