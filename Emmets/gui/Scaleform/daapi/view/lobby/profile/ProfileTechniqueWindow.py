# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileTechniqueWindow.py
from gui.Scaleform.daapi.view.lobby.profile.QueuedVehicleDossierReceiver import QueuedVehicleDossierReceiver
from gui.Scaleform.daapi.view.lobby.profile.ProfileTechnique import ProfileTechnique

class ProfileTechniqueWindow(ProfileTechnique):

    def __init__(self, *args):
        super(ProfileTechniqueWindow, self).__init__(*args)
        self.__dataReceiver = QueuedVehicleDossierReceiver()
        self.__currentlyRequestingVehicleId = None
        self.__dataReceiver.onDataReceived += self.__requestedDataReceived
        return

    def requestData(self, vehicleId):
        self.as_responseVehicleDossierS(None)
        self.__currentlyRequestingVehicleId = int(vehicleId)
        self.__dataReceiver.invoke(self._databaseID, self.__currentlyRequestingVehicleId)
        return

    def invokeUpdate(self):
        super(ProfileTechniqueWindow, self).invokeUpdate()
        if self._selectedVehicleIntCD is not None:
            self._receiveVehicleDossier(self._selectedVehicleIntCD, self._databaseID)
        return

    def _dispose(self):
        self.__dataReceiver.onDataReceived -= self.__requestedDataReceived
        self.__dataReceiver.dispose()
        self.__dataReceiver = None
        super(ProfileTechniqueWindow, self)._dispose()
        return

    def _setRatingButton(self):
        self.as_setRatingButtonS({'enabled': False, 'visible': False})

    def __requestedDataReceived(self, databaseID, vehicleID):
        if self.__currentlyRequestingVehicleId == vehicleID:
            self._receiveVehicleDossier(vehicleID, databaseID)