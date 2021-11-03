# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/avatar_components/warning_hints_controller.py
import Event
from helpers import dependency
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from skeletons.gui.battle_session import IBattleSessionProvider

class WarningHintsController(object):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        self.onAuraVictimNotification = Event.Event()
        self.onAuraVictimMarkerIcon = Event.Event()

    def onBecomePlayer(self):
        pass

    def onBecomeNonPlayer(self):
        pass

    def handleKey(self, isDown, key, mods):
        pass

    def showAuraSoulsWarningHint(self):
        self.onAuraVictimNotification(show=True)
        self.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.LOSE_SOULS_IN_AURA, True)

    def showAuraHealthWarningHint(self):
        self.onAuraVictimNotification(show=True)
        self.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.FIRE_WITH_MESSAGE, True)

    def hideAuraWarningHint(self):
        self.onAuraVictimNotification(show=False)
        self.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.FIRE_WITH_MESSAGE, False)
        self.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.LOSE_SOULS_IN_AURA, False)

    def showAuraVictimMarkerIcon(self, vehicleId):
        self.onAuraVictimMarkerIcon(show=True, vehicleId=vehicleId)

    def hideAuraVictimMarkerIcon(self, vehicleId):
        self.onAuraVictimMarkerIcon(show=False, vehicleId=vehicleId)