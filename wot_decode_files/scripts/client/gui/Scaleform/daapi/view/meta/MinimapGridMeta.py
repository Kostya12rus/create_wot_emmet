# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MinimapGridMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class MinimapGridMeta(BaseDAAPIComponent):

    def setClick(self, x, y):
        self._printOverrideError('setClick')

    def as_clickEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_clickEnabled(value)

    def as_addPointS(self, x, y):
        if self._isDAAPIInited():
            return self.flashObject.as_addPoint(x, y)

    def as_clearPointsS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_clearPoints()