# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LobbyVehicleMarkerViewMeta.py
from gui.Scaleform.framework.entities.View import View

class LobbyVehicleMarkerViewMeta(View):

    def onMarkerClick(self, id):
        self._printOverrideError('onMarkerClick')

    def as_createMarkerS(self, id, vType, vName, styleId=1):
        if self._isDAAPIInited():
            return self.flashObject.as_createMarker(id, vType, vName, styleId)

    def as_createPlatoonMarkerS(self, id, vType, pName):
        if self._isDAAPIInited():
            return self.flashObject.as_createPlatoonMarker(id, vType, pName)

    def as_createCustomMarkerS(self, id, icon, text):
        if self._isDAAPIInited():
            return self.flashObject.as_createCustomMarker(id, icon, text)

    def as_removeMarkerS(self, id):
        if self._isDAAPIInited():
            return self.flashObject.as_removeMarker(id)