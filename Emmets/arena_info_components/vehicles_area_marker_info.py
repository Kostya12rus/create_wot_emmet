# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/arena_info_components/vehicles_area_marker_info.py


class VehiclesAreaMarkerInfo(object):

    def onEnterWorld(self):
        self._setVehiclesAreaMarkerParams()

    def onLeaveWorld(self):
        pass

    def set_vehiclesAreaMarkerParams(self, _):
        self._setVehiclesAreaMarkerParams()

    def _setVehiclesAreaMarkerParams(self):
        areaMarkerCtrl = self.sessionProvider.shared.areaMarker
        if self.vehiclesAreaMarkerParams is not None and areaMarkerCtrl:
            areaMarkerCtrl.setVehiclesAreaMarkerParams(self.vehiclesAreaMarkerParams)
        return