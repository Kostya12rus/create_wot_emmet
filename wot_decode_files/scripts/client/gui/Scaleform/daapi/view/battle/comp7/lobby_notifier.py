# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/comp7/lobby_notifier.py
import BigWorld
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView
from constants import ARENA_PERIOD
_NOTIFICATION_TIME = 30.0

class LobbyNotifier(IAbstractPeriodView):

    def __init__(self):
        super(LobbyNotifier, self).__init__()
        self.__isNotified = False

    def setCountdown(self, state, timeLeft):
        if state == ARENA_PERIOD.PREBATTLE and timeLeft <= _NOTIFICATION_TIME:
            self.__doNotify()

    def __doNotify(self):
        if not self.__isNotified:
            BigWorld.WGWindowsNotifier.onBattleBeginning()
            self.__isNotified = True