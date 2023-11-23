# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/PoiVehicleComponent.py
from PoiBaseComponent import PoiBaseComponent
from points_of_interest.components import PoiVehicleStateComponent

class PoiVehicleComponent(PoiBaseComponent):

    def __init__(self):
        super(PoiVehicleComponent, self).__init__()
        self.__stateComponent = None
        self.__isDead = False
        return

    def onDestroy(self):
        self._poiGameObject.removeComponent(self.__stateComponent)
        self.__stateComponent = None
        self.__isDead = True
        super(PoiVehicleComponent, self).onDestroy()
        return

    def _onAvatarReady(self):
        if not self.__isDead:
            self.__stateComponent = self._poiGameObject.createComponent(PoiVehicleStateComponent, self.pointID)