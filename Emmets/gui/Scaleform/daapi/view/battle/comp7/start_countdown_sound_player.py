# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/comp7/start_countdown_sound_player.py
from constants import VEHICLE_SELECTION_BLOCK_DELAY
from gui.Scaleform.daapi.view.battle.shared.start_countdown_sound_player import StartCountdownSoundPlayer
from gui.battle_control.battle_constants import COUNTDOWN_STATE

class Comp7StartTimerSoundPlayer(StartCountdownSoundPlayer):

    def setCountdown(self, state, timeLeft):
        correctedTimeLeft = timeLeft - VEHICLE_SELECTION_BLOCK_DELAY if timeLeft is not None else timeLeft
        if correctedTimeLeft < 0:
            state = COUNTDOWN_STATE.STOP
        super(Comp7StartTimerSoundPlayer, self).setCountdown(state, correctedTimeLeft)
        return