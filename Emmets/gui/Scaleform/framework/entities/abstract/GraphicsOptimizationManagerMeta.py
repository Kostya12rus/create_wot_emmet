# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/GraphicsOptimizationManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class GraphicsOptimizationManagerMeta(BaseDAAPIComponent):

    def registerOptimizationArea(self, x, y, width, height):
        self._printOverrideError('registerOptimizationArea')

    def unregisterOptimizationArea(self, optimizationID):
        self._printOverrideError('unregisterOptimizationArea')

    def updateOptimizationArea(self, optimizationID, x, y, width, height):
        self._printOverrideError('updateOptimizationArea')

    def isOptimizationAvailable(self, alias):
        self._printOverrideError('isOptimizationAvailable')

    def isOptimizationEnabled(self, alias):
        self._printOverrideError('isOptimizationEnabled')

    def switchOptimizationEnabled(self, value):
        self._printOverrideError('switchOptimizationEnabled')

    def as_invalidateRectanglesS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_invalidateRectangles()

    def as_switchOptimizationEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_switchOptimizationEnabled(value)