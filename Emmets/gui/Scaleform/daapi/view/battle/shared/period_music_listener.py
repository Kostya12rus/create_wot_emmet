# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/period_music_listener.py
import WWISE, BattleReplay
from constants import ARENA_PERIOD
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView

class PeriodMusicListener(IAbstractPeriodView):
    _ARENA_PERIOD_STATE = {ARENA_PERIOD.WAITING: 'STATE_arenastate_waiting', 
       ARENA_PERIOD.PREBATTLE: 'STATE_arenastate_counter', 
       ARENA_PERIOD.BATTLE: 'STATE_arenastate_battle'}
    _STATE_ID = 'STATE_arenastate'

    def setPeriod(self, period):
        if BattleReplay.g_replayCtrl.isTimeWarpInProgress and period in (ARENA_PERIOD.WAITING, ARENA_PERIOD.PREBATTLE):
            return
        else:
            state_value = self._ARENA_PERIOD_STATE.get(period, None)
            if state_value is not None:
                WWISE.WW_setState(self._STATE_ID, state_value)
            return