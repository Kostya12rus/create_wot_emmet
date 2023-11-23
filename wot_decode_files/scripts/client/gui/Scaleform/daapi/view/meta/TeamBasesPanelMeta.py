# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TeamBasesPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TeamBasesPanelMeta(BaseDAAPIComponent):

    def as_addS(self, barId, sortWeight, colorType, title, points, captureTime, vehiclesCount):
        if self._isDAAPIInited():
            return self.flashObject.as_add(barId, sortWeight, colorType, title, points, captureTime, vehiclesCount)

    def as_removeS(self, id):
        if self._isDAAPIInited():
            return self.flashObject.as_remove(id)

    def as_stopCaptureS(self, id, points):
        if self._isDAAPIInited():
            return self.flashObject.as_stopCapture(id, points)

    def as_updateCaptureDataS(self, id, points, rate, captureTime, vehiclesCount, captureString, colorType):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCaptureData(id, points, rate, captureTime, vehiclesCount, captureString, colorType)

    def as_setCapturedS(self, id, title):
        if self._isDAAPIInited():
            return self.flashObject.as_setCaptured(id, title)

    def as_setOffsetForEnemyPointsS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_setOffsetForEnemyPoints()

    def as_clearS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_clear()