# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/arena_camera_manager.py
import CGF
from GenericComponents import TransformComponent
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery, autoregister
from CameraComponents import CameraComponent

@autoregister(presentInAllWorlds=True, domain=CGF.DomainOption.DomainClient)
class ArenaCameraManager(CGF.ComponentManager):

    def __init__(self, *args):
        super(ArenaCameraManager, self).__init__(*args)
        self.__cameras = dict()

    def getCameraTransform(self, name):
        return self.__cameras.get(name)

    @onAddedQuery(CameraComponent, TransformComponent, tickGroup='preInitGroup')
    def onCameraAdded(self, cameraComponent, transformComponent):
        self.__cameras[cameraComponent.name] = transformComponent.worldTransform

    @onRemovedQuery(CameraComponent, tickGroup='preInitGroup')
    def onCameraRemoved(self, cameraComponent):
        self.__cameras.pop(cameraComponent.name)