# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/hover_component.py
import BigWorld, CGF, GUI
from GenericComponents import VSEComponent
from cgf_script.managers_registrator import tickGroup, onAddedQuery, onRemovedQuery
from cgf_script.component_meta_class import registerComponent
from constants import IS_CLIENT
from vehicle_systems.tankStructure import ColliderTypes
from helpers import dependency
from skeletons.gui.shared.utils import IHangarSpace
if IS_CLIENT:
    from AvatarInputHandler import cameras

@registerComponent
class IsHovered(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor


class HoverManager(CGF.ComponentManager):
    _hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self):
        super(HoverManager, self).__init__()
        self.__enabled = True

    def enable(self):
        self.__enabled = True

    def disable(self):
        self.__enabled = False

    @onAddedQuery(VSEComponent, IsHovered)
    def onIsHoveredAdded(self, vseComponent, *args):
        vseComponent.context.onGameObjectHoverIn()

    @onRemovedQuery(VSEComponent, IsHovered)
    def onIsHoveredRemoved(self, vseComponent, *args):
        vseComponent.context.onGameObjectHoverOut()

    @tickGroup(groupName='Simulation')
    def tick(self):
        if not self.__enabled or not GUI.mcursor().inWindow or not GUI.mcursor().inFocus or not self._hangarSpace.isCursorOver3DScene or not self._hangarSpace.isSelectionEnabled:
            return
        cursorPosition = GUI.mcursor().position
        ray, wpoint = cameras.getWorldRayAndPoint(cursorPosition.x, cursorPosition.y)
        collidedId = None
        res = BigWorld.wg_collideDynamicStatic(self.spaceID, wpoint, wpoint + ray * 1000, 0, 0, -1, ColliderTypes.HANGAR_FLAG)
        if res is not None:
            collidedId = res[2]
        gameObjects = CGF.Query(self.spaceID, CGF.GameObject)
        for gameObject in gameObjects:
            if gameObject.id == collidedId:
                self._updateHoverComponent(gameObject, True)
            else:
                self._updateHoverComponent(gameObject, False)

        return

    def _updateHoverComponent(self, go, isHovered):
        if isHovered:
            if go.findComponentByType(IsHovered) is None:
                go.createComponent(IsHovered)
        else:
            go.removeComponentByType(IsHovered)
        return