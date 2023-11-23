# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/stronghold/plugins.py
from gui.Scaleform.daapi.view.battle.shared.markers2d.vehicle_plugins import VehicleMarkerPlugin
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES as _STATES

class _StrongholdInspireMarker(object):
    __slots__ = ('isSourceVehicle', 'isInactivation')

    def __init__(self, isSourceVehicle, isInactivation):
        self.isSourceVehicle = isSourceVehicle
        self.isInactivation = isInactivation

    def needInspireCounter(self):
        return self.isSourceVehicle

    def getHideStatusID(self):
        if self.needInspireCounter():
            return _STATES.INSPIRED_STATE
        return _STATES.INSPIRING_STATE

    def getStatusID(self):
        if self.needInspireCounter():
            return _STATES.INSPIRING_STATE
        return _STATES.INSPIRED_STATE


class StrongholdVehicleMarkerPlugin(VehicleMarkerPlugin):

    def _updateInspireMarker(self, vehicleID, handle, isSourceVehicle, isInactivation, endTime, duration, primary=True, animated=True, equipmentID=None):
        inspireMarker = _StrongholdInspireMarker(isSourceVehicle, isInactivation)
        if isInactivation is not None:
            statusID = inspireMarker.getStatusID()
            hideStatusID = inspireMarker.getHideStatusID()
            if inspireMarker.needInspireCounter():
                self._updateMarkerTimer(vehicleID, handle, duration, statusID)
            self._updateStatusMarkerState(vehicleID, False, handle, hideStatusID, duration, animated, bool(isSourceVehicle))
            self._updateStatusMarkerState(vehicleID, True, handle, statusID, duration, animated, bool(isSourceVehicle))
        else:
            self._updateStatusMarkerState(vehicleID, False, handle, _STATES.INSPIRED_STATE, 0, animated, False)
            self._updateStatusMarkerState(vehicleID, False, handle, _STATES.INSPIRING_STATE, 0, animated, False)
        return