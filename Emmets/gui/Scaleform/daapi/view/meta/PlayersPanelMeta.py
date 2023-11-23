# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PlayersPanelMeta.py
from gui.Scaleform.daapi.view.battle.shared.base_stats import StatsBase

class PlayersPanelMeta(StatsBase):

    def tryToSetPanelModeByMouse(self, panelMode):
        self._printOverrideError('tryToSetPanelModeByMouse')

    def switchToOtherPlayer(self, vehicleID):
        self._printOverrideError('switchToOtherPlayer')

    def as_setPanelModeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPanelMode(value)

    def as_setChatCommandsVisibilityS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setChatCommandsVisibility(value)

    def as_setPlayerHPS(self, isAlly, index, percent):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerHP(isAlly, index, percent)

    def as_setOverrideExInfoS(self, exOverrideInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_setOverrideExInfo(exOverrideInfo)

    def as_setPanelHPBarVisibilityStateS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPanelHPBarVisibilityState(value)