# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/PoiBaseComponent.py
from helpers import dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider

class PoiBaseComponent(DynamicScriptComponent):
    _POI_GO_NAME = 'PointOfInterest{id}'
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(PoiBaseComponent, self).__init__()
        self._poiGameObject = self.__getPoiGameObject()

    def onLeaveWorld(self):
        self._poiGameObject = None
        return

    def __getPoiGameObject(self):
        name = self._POI_GO_NAME.format(id=self.pointID)
        poiCtrl = self.__sessionProvider.dynamic.pointsOfInterest
        return poiCtrl.getVehicleCapturingPoiGO(name, self.entity.entityGameObject, self.entity.id, self.spaceID)