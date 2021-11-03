# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/event/event_phase_indicator.py
from gui.Scaleform.daapi.view.battle.event.game_event_getter import GameEventGetterMixin
from gui.Scaleform.daapi.view.meta.PhaseIndicatorMeta import PhaseIndicatorMeta

class EventPhaseIndicator(PhaseIndicatorMeta, GameEventGetterMixin):

    def __init__(self):
        super(EventPhaseIndicator, self).__init__()
        self._isVisible = False

    def _populate(self):
        if self.environmentData is not None:
            self.environmentData.onUpdated += self.__onEnvironmentChanged
            self.__onEnvironmentChanged()
        else:
            self._setVisible(False)
        return

    def _dispose(self):
        if self.environmentData is not None:
            self.environmentData.onUpdated -= self.__onEnvironmentChanged
        return

    def _setVisible(self, value):
        if self._isVisible != value:
            self._isVisible = value
            self.as_setVisibleS(value)

    def __onEnvironmentChanged(self):
        if not self.environmentData.hasSyncData():
            self._setVisible(False)
        else:
            self._setVisible(True)
            envID = self.__getEnvironmentId()
            maxPhase = self.__getPhaseNumber(self.__getEnvironmentMax())
            currentPhase = min(self.__getPhaseNumber(envID), maxPhase)
            self.as_setDataS(currentPhase, maxPhase)

    def __getEnvironmentId(self):
        if self.environmentData is None:
            return 0
        else:
            return self.environmentData.getCurrentEnvironmentID()

    def __getEnvironmentMax(self):
        if self.environmentData is None:
            return 0
        else:
            return self.environmentData.getMaxEnvironmentID()

    def __getPhaseNumber(self, envID):
        envList = self.environmentData.getEnvironmentsList()
        envsOrder = [ x['id'] for x in envList ]
        envIndex = envsOrder.index(envID) if envID in envsOrder else 0
        return envIndex + 1