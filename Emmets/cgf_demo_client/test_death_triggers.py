# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_demo_client/test_death_triggers.py
import logging
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent
from cgf_script.managers_registrator import autoregister, onAddedQuery
from cgf_demo.demo_category import DEMO_CATEGORY
import CGF, functools
from HealthComponents import DeathComponent
from Triggers import AreaTriggerComponent
_logger = logging.getLogger(__name__)

@registerComponent
class TestAddDeathByTrigger(object):
    category = DEMO_CATEGORY
    domain = CGF.DomainOption.DomainClient
    goLink = ComponentProperty(type=CGFMetaTypes.LINK, editorName='goLink', value=CGF.GameObject)


@registerComponent
class TestRemoveDeathByTrigger(object):
    category = DEMO_CATEGORY
    domain = CGF.DomainOption.DomainClient
    goLink = ComponentProperty(type=CGFMetaTypes.LINK, editorName='goLink', value=CGF.GameObject)


@autoregister(presentInAllWorlds=True, category=DEMO_CATEGORY)
class TestDeathByTriggerManager(CGF.ComponentManager):

    @onAddedQuery(CGF.GameObject, AreaTriggerComponent, TestAddDeathByTrigger)
    def onAddedAddDeath(self, go, trigger, addDeath):
        trigger.addEnterReaction(functools.partial(self.__addDeath, addDeath.goLink))

    @onAddedQuery(CGF.GameObject, AreaTriggerComponent, TestRemoveDeathByTrigger)
    def onAddedRemoveDeath(self, go, trigger, removeDeath):
        trigger.addEnterReaction(functools.partial(self.__removeDeath, removeDeath.goLink))

    def __addDeath(self, go):
        if not go.findComponentByType(DeathComponent):
            go.createComponent(DeathComponent)

    def __removeDeath(self, go):
        if go.findComponentByType(DeathComponent):
            go.removeComponent(DeathComponent)