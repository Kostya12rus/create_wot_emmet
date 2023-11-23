# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EventBoardsAwardsOverlayMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EventBoardsAwardsOverlayMeta(BaseDAAPIComponent):

    def changeFilter(self, id):
        self._printOverrideError('changeFilter')

    def as_setHeaderS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeader(data)

    def as_setVehicleS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicle(data)

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)