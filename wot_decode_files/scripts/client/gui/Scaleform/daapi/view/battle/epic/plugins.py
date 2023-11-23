# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/epic/plugins.py
from gui.Scaleform.daapi.view.battle.shared.markers2d.vehicle_plugins import VehicleMarkerPlugin
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES
_EPIC_STATUS_EFFECTS_PRIORITY = (
 BATTLE_MARKER_STATES.STUN_STATE,
 BATTLE_MARKER_STATES.FL_REGENERATION_KIT_STATE,
 BATTLE_MARKER_STATES.REPAIRING_STATE,
 BATTLE_MARKER_STATES.ENGINEER_STATE,
 BATTLE_MARKER_STATES.HEALING_STATE,
 BATTLE_MARKER_STATES.BERSERKER_STATE,
 BATTLE_MARKER_STATES.STEALTH_STATE,
 BATTLE_MARKER_STATES.INSPIRING_STATE,
 BATTLE_MARKER_STATES.DEBUFF_STATE,
 BATTLE_MARKER_STATES.INSPIRED_STATE)

class EpicVehicleMarkerPlugin(VehicleMarkerPlugin):

    def _getMarkerStatusPriority(self, markerState):
        try:
            return _EPIC_STATUS_EFFECTS_PRIORITY.index(markerState.statusID)
        except ValueError:
            return -1


class EpicRespawnableVehicleMarkerPlugin(EpicVehicleMarkerPlugin):

    def start(self):
        super(EpicRespawnableVehicleMarkerPlugin, self).start()
        self._isSquadIndicatorEnabled = False

    def _hideVehicleMarker(self, vehicleID):
        self._destroyVehicleMarker(vehicleID)