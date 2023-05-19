# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCLobbyVehicleMarkerView.py
from gui.impl.gen import R
from gui.Scaleform.daapi.view.lobby.lobby_vehicle_marker_view import LobbyVehicleMarkerView
from gui.shared import EVENT_BUS_SCOPE
from gui.shared.events import HangarVehicleEvent

class BCLobbyVehicleMarkerView(LobbyVehicleMarkerView):

    def _populate(self):
        self.addListener(HangarVehicleEvent.BOOTCAMP_SECOND_TANK_MARKER, self._onBootcampSecondTankMarker, EVENT_BUS_SCOPE.LOBBY)
        super(BCLobbyVehicleMarkerView, self)._populate()

    def _dispose(self):
        self.removeListener(HangarVehicleEvent.BOOTCAMP_SECOND_TANK_MARKER, self._onBootcampSecondTankMarker, EVENT_BUS_SCOPE.LOBBY)
        super(BCLobbyVehicleMarkerView, self)._dispose()

    def _onBootcampSecondTankMarker(self, event):
        if event.ctx['isVisible']:
            self._onPlatoonTankLoaded(event)
        else:
            self._onHeroPlatoonTankDestroy(event)

    def _canShowMarkers(self):
        windowsManager = self.guiLoader.windowsManager
        if windowsManager.getViewByLayoutID(R.views.lobby.bootcamp.BootcampNationView()) is not None:
            return True
        else:
            return super(BCLobbyVehicleMarkerView, self)._canShowMarkers()

    def as_createPlatoonMarkerS(self, id, _, pName):
        return super(BCLobbyVehicleMarkerView, self).as_createPlatoonMarkerS(id, '', pName)