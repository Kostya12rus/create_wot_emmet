# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/AttackArtilleryFort.py
import BigWorld, Math
from AreaOfEffect import AreaOfEffect
from account_helpers.settings_core.settings_constants import GRAPHICS
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore

class AttackArtilleryFort(AreaOfEffect):
    __settingsCore = dependency.descriptor(ISettingsCore)

    @property
    def areaColor(self):
        arenaDP = self.sessionProvider.getArenaDP()
        if arenaDP is not None and not arenaDP.isAllyTeam(self.team):
            if self.__settingsCore.getSetting(GRAPHICS.COLOR_BLIND) and self._equipment.enemyAreaColorBlind is not None:
                return self._equipment.enemyAreaColorBlind
            return self._equipment.enemyAreaColor
        else:
            return super(AttackArtilleryFort, self).areaColor

    @property
    def _direction(self):
        return Math.Vector3(1, 0, 0)

    def _showMarker(self):
        delay = self.strikeTime - BigWorld.serverTime()
        equipmentsCtrl = self.sessionProvider.shared.equipments
        if equipmentsCtrl and delay > 0:
            equipmentsCtrl.showMarker(self._equipment, self.position, self._direction, delay, self.team)