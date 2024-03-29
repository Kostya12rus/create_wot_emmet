# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleMarkersManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class VehicleMarkersManagerMeta(BaseDAAPIComponent):

    def as_setMarkerDurationS(self, duration):
        if self._isDAAPIInited():
            return self.flashObject.as_setMarkerDuration(duration)

    def as_setMarkerSettingsS(self, settings):
        if self._isDAAPIInited():
            return self.flashObject.as_setMarkerSettings(settings)

    def as_setShowExInfoFlagS(self, flag):
        if self._isDAAPIInited():
            return self.flashObject.as_setShowExInfoFlag(flag)

    def as_updateMarkersSettingsS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_updateMarkersSettings()

    def as_setColorBlindS(self, isColorBlind):
        if self._isDAAPIInited():
            return self.flashObject.as_setColorBlind(isColorBlind)

    def as_setColorSchemesS(self, defaultSchemes, colorBlindSchemes):
        if self._isDAAPIInited():
            return self.flashObject.as_setColorSchemes(defaultSchemes, colorBlindSchemes)