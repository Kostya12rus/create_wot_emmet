# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_demo_client/test_physical_debris_spawner.py
import functools, CGF, Triggers, Physics
from cgf_demo.demo_category import DEMO_CATEGORY
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent
from cgf_script.managers_registrator import onAddedQuery

@registerComponent
class TestEntranceSpawner(object):
    category = DEMO_CATEGORY
    domain = CGF.DomainOption.DomainClient
    trigger = ComponentProperty(type=CGFMetaTypes.LINK, editorName='AreaTrigger to subscribe', value=Triggers.AreaTriggerComponent)
    debrisSpawner = ComponentProperty(type=CGFMetaTypes.LINK, editorName='Spawner to subscribe', value=Physics.PhysicalDebrisSpawnerComponent)


class EntranceSpawnerManager(CGF.ComponentManager):

    @onAddedQuery(TestEntranceSpawner)
    def onEntranceAdded(self, entrance):
        trigger = entrance.trigger()
        if trigger:
            trigger.addEnterReaction(functools.partial(self.__onEnter, entrance))
            trigger.addExitReaction(functools.partial(self.__onExit, entrance))

    def __onEnter(self, entrance, who, where):
        spawner = entrance.debrisSpawner()
        if spawner:
            spawner.spawnDebris(True)

    def __onExit(self, entrance, who, where):
        spawner = entrance.debrisSpawner()
        if spawner:
            spawner.removeDebris()