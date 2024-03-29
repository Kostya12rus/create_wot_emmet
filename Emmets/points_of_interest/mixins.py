# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/points_of_interest/mixins.py
import typing, CGF
from points_of_interest.components import PoiStateComponent, PoiStateUIListenerComponent, PoiVehicleStateComponent
from shared_utils import first
from gui.battle_control import avatar_getter

class PointsOfInterestListener(object):

    def __init__(self):
        self.__listenerGameObject = None
        return

    @property
    def _poiStateQuery(self):
        spaceID = avatar_getter.getSpaceID()
        if spaceID is not None:
            return CGF.Query(spaceID, PoiStateComponent)
        else:
            return []

    @property
    def _poiVehicleState(self):
        spaceID = avatar_getter.getSpaceID()
        if spaceID is not None:
            return first(CGF.Query(spaceID, PoiVehicleStateComponent))
        else:
            return

    def onPoiAdded(self, state):
        pass

    def onPoiRemoved(self, state):
        pass

    def onProcessPoi(self, state):
        pass

    def onPoiEntered(self, poiID):
        pass

    def onPoiLeft(self, poiID):
        pass

    def _registerPoiListener(self, go=None):
        spaceID = avatar_getter.getSpaceID()
        if spaceID is None:
            return
        else:
            if go is None:
                self.__listenerGameObject = go = CGF.GameObject(spaceID, self.__class__.__name__)
                go.activate()
            go.createComponent(PoiStateUIListenerComponent, self)
            return

    def _unregisterPoiListener(self, go=None):
        if go is not None:
            go.removeComponentByType(PoiStateUIListenerComponent)
        elif self.__listenerGameObject is not None:
            if self.__listenerGameObject.isValid():
                self.__listenerGameObject.destroy()
            self.__listenerGameObject = None
        return