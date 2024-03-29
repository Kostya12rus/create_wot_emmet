# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MinimapPresentationMeta.py
from gui.Scaleform.daapi.view.meta.MinimapEntityMeta import MinimapEntityMeta

class MinimapPresentationMeta(MinimapEntityMeta):

    def setMap(self, arenaID):
        self._printOverrideError('setMap')

    def setMinimapData(self, arenaID, playerTeam, size):
        self._printOverrideError('setMinimapData')

    def as_changeMapS(self, texture):
        if self._isDAAPIInited():
            return self.flashObject.as_changeMap(texture)

    def as_addPointS(self, x, y, type, color, id):
        if self._isDAAPIInited():
            return self.flashObject.as_addPoint(x, y, type, color, id)

    def as_addPoiS(self, x, y, type, id):
        if self._isDAAPIInited():
            return self.flashObject.as_addPoi(x, y, type, id)

    def as_clearS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_clear()