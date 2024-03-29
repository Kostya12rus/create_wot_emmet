# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortClanBattleRoomMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyRoomView import BaseRallyRoomView

class FortClanBattleRoomMeta(BaseRallyRoomView):

    def onTimerAlert(self):
        self._printOverrideError('onTimerAlert')

    def openConfigureWindow(self):
        self._printOverrideError('openConfigureWindow')

    def toggleRoomStatus(self):
        self._printOverrideError('toggleRoomStatus')

    def onFiltersChange(self, slotIndex, filters):
        self._printOverrideError('onFiltersChange')

    def resetFilters(self, slotIndex):
        self._printOverrideError('resetFilters')

    def as_updateTeamHeaderTextS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTeamHeaderText(value)

    def as_setBattleRoomDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBattleRoomData(data)

    def as_updateReadyStatusS(self, mineValue, enemyValue):
        if self._isDAAPIInited():
            return self.flashObject.as_updateReadyStatus(mineValue, enemyValue)

    def as_updateReadyDirectionsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateReadyDirections(value)

    def as_setConfigureButtonStateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setConfigureButtonState(data)

    def as_setTimerDeltaS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimerDelta(data)

    def as_setDirectionS(self, value, animationNotAvailable):
        if self._isDAAPIInited():
            return self.flashObject.as_setDirection(value, animationNotAvailable)

    def as_setReservesEnabledS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setReservesEnabled(data)

    def as_setReservesDataS(self, reservesData):
        if self._isDAAPIInited():
            return self.flashObject.as_setReservesData(reservesData)

    def as_setOpenedS(self, buttonLabel, statusLabel, tooltipLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_setOpened(buttonLabel, statusLabel, tooltipLabel)

    def as_setTableHeaderS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setTableHeader(data)

    def as_setFiltersDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setFiltersData(data)