# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MinimapMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class MinimapMeta(BaseDAAPIComponent):

    def onMinimapClicked(self, x, y, buttonIdx, mapScaleIndex):
        self._printOverrideError('onMinimapClicked')

    def applyNewSize(self, sizeIndex):
        self._printOverrideError('applyNewSize')

    def as_setSizeS(self, size):
        if self._isDAAPIInited():
            return self.flashObject.as_setSize(size)

    def as_setVisibleS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(isVisible)

    def as_setAlphaS(self, alpha):
        if self._isDAAPIInited():
            return self.flashObject.as_setAlpha(alpha)

    def as_showVehiclesNameS(self, visibility):
        if self._isDAAPIInited():
            return self.flashObject.as_showVehiclesName(visibility)

    def as_setBackgroundS(self, path):
        if self._isDAAPIInited():
            return self.flashObject.as_setBackground(path)

    def as_enableHintPanelWithDataS(self, isStrategicArtyView, isSPG):
        if self._isDAAPIInited():
            return self.flashObject.as_enableHintPanelWithData(isStrategicArtyView, isSPG)

    def as_disableHintPanelS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_disableHintPanel()

    def as_updateHintPanelDataS(self, isStrategicArtyView, isSPG):
        if self._isDAAPIInited():
            return self.flashObject.as_updateHintPanelData(isStrategicArtyView, isSPG)