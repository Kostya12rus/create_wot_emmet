# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/new_year/cgf_components/current_camera_object_manager.py
import BigWorld, CGF
from cgf_script.component_meta_class import CGFComponent
from cgf_script.managers_registrator import onAddedQuery, autoregister
from gui.impl.new_year.navigation import NewYearNavigation
from helpers import dependency
from new_year.cgf_components.highlight_manager import IsHighlighted, HighlightComponent
from new_year.ny_constants import ANCHOR_TO_OBJECT
from skeletons.gui.shared.utils import IHangarSpace

class CurrentCameraObject(CGFComponent):
    pass


@autoregister(presentInAllWorlds=True)
class CurrentCameraObjectManager(CGF.ComponentManager):
    _hangarSpace = dependency.descriptor(IHangarSpace)

    @onAddedQuery(CurrentCameraObject, CGF.GameObject)
    def onIsCameraObjectAdded(self, _, go):
        go.removeComponentByType(IsHighlighted)

    @onAddedQuery(HighlightComponent)
    def onHighlightComponentAdded(self, highlightComponent):
        addedNavigationName = ANCHOR_TO_OBJECT.get(getattr(highlightComponent.owner, 'anchorName', None))
        if addedNavigationName and addedNavigationName == NewYearNavigation.getCurrentObject():
            highlightComponent.owner.entityGameObject.createComponent(CurrentCameraObject)
        return

    @classmethod
    def switchCameraToAnchor(cls, anchorName):
        if cls._hangarSpace.space is None:
            return
        else:
            isCameraQuery = CGF.Query(cls._hangarSpace.spaceID, (CGF.GameObject, CurrentCameraObject))
            for go, _ in isCameraQuery:
                go.removeComponentByType(CurrentCameraObject)

            for entity in BigWorld.entities.values():
                if cls.__filterEntity(entity, anchorName):
                    if entity.entityGameObject.findComponentByType(CurrentCameraObject) is None:
                        entity.entityGameObject.createComponent(CurrentCameraObject)

            return

    @classmethod
    def __filterEntity(cls, entity, anchorName):
        if anchorName is not None and getattr(entity, 'anchorName', None) == anchorName:
            return True
        else:
            if anchorName is None and cls._hangarSpace.space.getVehicleEntity() == entity:
                return True
            return False