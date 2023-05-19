# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/PoiVehicleComponent.py
from PoiBaseComponent import PoiBaseComponent
from points_of_interest.components import PoiVehicleStateComponent

class PoiVehicleComponent(PoiBaseComponent):

    def __init__(self):
        super(PoiVehicleComponent, self).__init__()
        self.__stateComponent = None
        return

    def onDestroy(self):
        self._poiGameObject.removeComponent(self.__stateComponent)
        self.__stateComponent = None
        super(PoiVehicleComponent, self).onDestroy()
        return

    def _onAvatarReady(self):
        self.__stateComponent = self._poiGameObject.createComponent(PoiVehicleStateComponent, self.pointID)