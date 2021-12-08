# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/ContainerManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ContainerManagerMeta(BaseDAAPIComponent):

    def isModalViewsIsExists(self):
        self._printOverrideError('isModalViewsIsExists')

    def as_getViewS(self, name):
        if self._isDAAPIInited():
            return self.flashObject.as_getView(name)

    def as_showS(self, name, x=0, y=0):
        if self._isDAAPIInited():
            return self.flashObject.as_show(name, x, y)

    def as_registerContainerS(self, layer, name):
        if self._isDAAPIInited():
            return self.flashObject.as_registerContainer(layer, name)

    def as_unregisterContainerS(self, layer):
        if self._isDAAPIInited():
            return self.flashObject.as_unregisterContainer(layer)

    def as_closePopUpsS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_closePopUps()

    def as_isOnTopS(self, layer, windowName):
        if self._isDAAPIInited():
            return self.flashObject.as_isOnTop(layer, windowName)

    def as_bringToFrontS(self, layer, windowName):
        if self._isDAAPIInited():
            return self.flashObject.as_bringToFront(layer, windowName)

    def as_showContainersS(self, layers, time=0):
        if self._isDAAPIInited():
            return self.flashObject.as_showContainers(layers, time)

    def as_hideContainersS(self, layers, time=0):
        if self._isDAAPIInited():
            return self.flashObject.as_hideContainers(layers, time)

    def as_isContainerShownS(self, layer):
        if self._isDAAPIInited():
            return self.flashObject.as_isContainerShown(layer)

    def as_getVisibleLayersS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getVisibleLayers()

    def as_setVisibleLayersS(self, layers):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisibleLayers(layers)

    def as_setContainersVisibleS(self, visible, excludes):
        if self._isDAAPIInited():
            return self.flashObject.as_setContainersVisible(visible, excludes)

    def as_storeContainersVisibleS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_storeContainersVisible()