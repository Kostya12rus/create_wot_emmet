# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/TeamInfoLivesComponent.py
import Event
from script_component.DynamicScriptComponent import DynamicScriptComponent

class TeamInfoLivesComponent(DynamicScriptComponent):
    onTeamLivesUpdated = Event.Event()

    def onEnterWorld(self, *args):
        self.onTeamLivesUpdated()

    def set_teamLives(self, prev):
        self.onTeamLivesUpdated()

    def getLives(self, vehicleID):
        return self.getVehicleLives(vehicleID).get('lives', 0)

    def getLockedLives(self, vehicleID):
        return self.getVehicleLives(vehicleID).get('lockedLives', 0)

    def getUsedLives(self, vehicleID):
        return self.getVehicleLives(vehicleID).get('usedLives', 0)

    def getVehicleLives(self, vehicleID):
        for vl in self.teamLives:
            if vl['vehicleID'] == vehicleID:
                return dict(vl)

        return {}