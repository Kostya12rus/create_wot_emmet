# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PointsOfInterestNotificationPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class PointsOfInterestNotificationPanelMeta(BaseDAAPIComponent):

    def as_addPoiStatusS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_addPoiStatus(data)

    def as_updatePoiStatusS(self, id, status, isAlly):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePoiStatus(id, status, isAlly)

    def as_updatePoiProgressS(self, id, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePoiProgress(id, progress)

    def as_addNotificationS(self, id, isAlly, message):
        if self._isDAAPIInited():
            return self.flashObject.as_addNotification(id, isAlly, message)

    def as_setReplaySpeedS(self, value=1):
        if self._isDAAPIInited():
            return self.flashObject.as_setReplaySpeed(value)