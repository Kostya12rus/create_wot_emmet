# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/avatar_components/vehicle_health_broadcast_listener_component.py
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class VehicleHealthBroadcastListenerComponent(object):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def onEnterWorld(self, prereqs=None):
        pass

    def onLeaveWorld(self):
        pass

    def handleKey(self, isDown, key, mods):
        pass

    def onBecomePlayer(self):
        pass

    def onBecomeNonPlayer(self):
        pass

    def onVehicleHealthChanged(self, vehicleID, newHealth, attackerID, attackReasonID):
        self.guiSessionProvider.setVehicleHealth(False, vehicleID, newHealth, attackerID, attackReasonID)