# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LobbyVehicleMarkerViewMeta.py
from gui.Scaleform.framework.entities.View import View

class LobbyVehicleMarkerViewMeta(View):

    def onMarkerClick(self, id):
        self._printOverrideError('onMarkerClick')

    def as_createMarkerS(self, id, vType, vName):
        if self._isDAAPIInited():
            return self.flashObject.as_createMarker(id, vType, vName)

    def as_createPlatoonMarkerS(self, id, vType, pName):
        if self._isDAAPIInited():
            return self.flashObject.as_createPlatoonMarker(id, vType, pName)

    def as_createCustomMarkerS(self, id, icon, text):
        if self._isDAAPIInited():
            return self.flashObject.as_createCustomMarker(id, icon, text)

    def as_removeMarkerS(self, id):
        if self._isDAAPIInited():
            return self.flashObject.as_removeMarker(id)