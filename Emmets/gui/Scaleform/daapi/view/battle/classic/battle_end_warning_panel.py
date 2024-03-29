# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/classic/battle_end_warning_panel.py
import WWISE
from gui.Scaleform.daapi.view.meta.BattleEndWarningPanelMeta import BattleEndWarningPanelMeta
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView
from helpers import dependency
from helpers.i18n import makeString as _ms
from helpers.time_utils import ONE_MINUTE
from skeletons.gui.battle_session import IBattleSessionProvider

class _WWISE_EVENTS(object):
    APPEAR = 'time_buzzer_01'


_WARNING_TEXT_KEY = '#ingame_gui:battleEndWarning/text'
_SWF_FILE_NAME = 'BattleEndWarningPanel.swf'
_CALLBACK_NAME = 'battle.onLoadEndWarningPanel'

class BattleEndWarningPanel(BattleEndWarningPanelMeta, IAbstractPeriodView):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(BattleEndWarningPanel, self).__init__()
        arenaVisitor = self.sessionProvider.arenaVisitor
        self.__duration = arenaVisitor.type.getBattleEndWarningDuration()
        self.__appearTime = arenaVisitor.type.getBattleEndWarningAppearTime()
        self.__roundLength = arenaVisitor.getRoundLength()
        self.__isShown = False
        self.__warningIsValid = self.__validateWarningTime()

    def isLoaded(self):
        return True

    def setTotalTime(self, totalTime):
        if not self.isLoaded():
            return
        minutes, seconds = divmod(int(totalTime), ONE_MINUTE)
        minutesStr = ('{:02d}').format(minutes)
        secondsStr = ('{:02d}').format(seconds)
        if self.__isShown:
            self.as_setTotalTimeS(minutesStr, secondsStr)
        if totalTime == self.__appearTime and self.__warningIsValid:
            self._callWWISE(_WWISE_EVENTS.APPEAR)
            self.as_setTotalTimeS(minutesStr, secondsStr)
            self.as_setTextInfoS(_ms(_WARNING_TEXT_KEY))
            self.as_setStateS(True)
            self.__isShown = True
        if (totalTime <= self.__appearTime - self.__duration or totalTime > self.__appearTime) and self.__isShown:
            self.as_setStateS(False)
            self.__isShown = False

    def _callWWISE(self, wwiseEventName):
        WWISE.WW_eventGlobal(wwiseEventName)

    def __validateWarningTime(self):
        if self.__appearTime < self.__duration or self.__appearTime <= 0 or self.__duration <= 0 or self.__appearTime > self.__roundLength or self.__duration > self.__roundLength and self.sessionProvider.arenaVisitor.isBattleEndWarningEnabled():
            return False
        return True