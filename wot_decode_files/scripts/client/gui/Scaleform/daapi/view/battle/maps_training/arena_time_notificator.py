# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/maps_training/arena_time_notificator.py
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
_TIME_TO_NOTIFY_BATTLE_END = 120

class MapsTrainingArenaTimeNotificator(IAbstractPeriodView):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(MapsTrainingArenaTimeNotificator, self).__init__()
        self.__prevLength = None
        self.__period = None
        self.__lastNotifiedTime = None
        return

    def setTotalTime(self, totalTime):
        if self.__lastNotifiedTime is None:
            self.__lastNotifiedTime = totalTime
        if totalTime == _TIME_TO_NOTIFY_BATTLE_END or totalTime < _TIME_TO_NOTIFY_BATTLE_END < self.__lastNotifiedTime:
            self.sessionProvider.dynamic.battleHints.showHint('timeRunsOut', {'param1': _TIME_TO_NOTIFY_BATTLE_END})
        self.__lastNotifiedTime = totalTime
        return