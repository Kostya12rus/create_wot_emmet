# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EpicMinimapMeta.py
from gui.Scaleform.daapi.view.battle.shared.minimap.component import MinimapComponent

class EpicMinimapMeta(MinimapComponent):

    def onZoomModeChanged(self, change):
        self._printOverrideError('onZoomModeChanged')

    def as_setZoomModeS(self, mode, modeText):
        if self._isDAAPIInited():
            return self.flashObject.as_setZoomMode(mode, modeText)

    def as_setMapDimensionsS(self, widthPx, heightPx):
        if self._isDAAPIInited():
            return self.flashObject.as_setMapDimensions(widthPx, heightPx)

    def as_updateSectorStateStatsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSectorStateStats(data)