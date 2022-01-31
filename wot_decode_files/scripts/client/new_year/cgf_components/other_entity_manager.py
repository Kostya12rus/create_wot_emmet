# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/new_year/cgf_components/other_entity_manager.py
import BigWorld, CGF, Math, math_utils
from GenericComponents import TransformComponent
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery
from cgf_script.component_meta_class import CGFComponent
from helpers import dependency
from skeletons.new_year import ICustomizableObjectsManager

class OtherEntityComponent(CGFComponent):

    def __init__(self, state, entityClass):
        super(OtherEntityComponent, self).__init__()
        self.state = state
        self.entityClass = entityClass
        self.entityID = None
        return


class OtherEntityManager(CGF.ComponentManager):
    __customizableObjectsMgr = dependency.descriptor(ICustomizableObjectsManager)

    @onAddedQuery(OtherEntityComponent, TransformComponent)
    def onEntityComponentAdded(self, entityComponent, transformComponent):
        scaleMatrix = math_utils.createRTMatrix(transformComponent.worldRotation, transformComponent.worldPosition)
        scaleMatrix.invert()
        scaleMatrix.preMultiply(transformComponent.worldTransform)
        scaleCoeffs = scaleMatrix.applyVector((1, 1, 1))
        state = {'scale': scaleCoeffs}
        state.update(entityComponent.state)
        rotationRPY = Math.Vector3(transformComponent.worldTransform.roll, transformComponent.worldTransform.pitch, transformComponent.worldTransform.yaw)
        entityComponent.entityID = BigWorld.createEntity(entityComponent.entityClass.__name__, self.spaceID, 0, transformComponent.worldPosition, rotationRPY, state)

    @onRemovedQuery(OtherEntityComponent, CGF.GameObject)
    def onEntityComponentRemoved(self, entityComponent, _):
        if entityComponent.entityID in BigWorld.entities.keys():
            BigWorld.destroyEntity(entityComponent.entityID)
        else:
            self.__customizableObjectsMgr.pendingEntitiesToDestroy.add(entityComponent.entityID)