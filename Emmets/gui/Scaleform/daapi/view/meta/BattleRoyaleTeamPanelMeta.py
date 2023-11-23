# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleRoyaleTeamPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleRoyaleTeamPanelMeta(BaseDAAPIComponent):

    def as_setInitDataS(self, title, names, clans):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(title, names, clans)

    def as_setPlayerStateS(self, index, alive, ready, hpPercent, fragsCount, vehicleLevel, icon):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerState(index, alive, ready, hpPercent, fragsCount, vehicleLevel, icon)

    def as_setPlayerStatusS(self, index, alive, ready, isRespawning=False):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerStatus(index, alive, ready, isRespawning)

    def as_setPlayerHPS(self, index, percent):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerHP(index, percent)

    def as_setPlayerFragsS(self, index, count):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerFrags(index, count)

    def as_setVehicleLevelS(self, index, level):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleLevel(index, level)

    def as_setPlayerVehicleS(self, index, icon):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerVehicle(index, icon)