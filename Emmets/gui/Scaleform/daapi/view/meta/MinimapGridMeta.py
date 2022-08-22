# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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