# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_demo_client/demo_rules.py
import CGF
from cgf_demo.demo_category import DEMO_CATEGORY
from cgf_demo_client.test_hierarchy_modificator import ModelSwapperManager
from cgf_demo_client.test_state_machine_trigger import StateMachineActivatorManager
from cgf_demo_client.test_triggers import EntranceModifierManager, TestHealthMonitoringManager
from cgf_script.managers_registrator import Rule, registerManager, registerRule
from cgf_demo_client.test_physical_debris_spawner import EntranceSpawnerManager
from constants import IS_CLIENT
if IS_CLIENT:
    from TestReplicableComponent import DisplayReplicableValuesManager
else:

    class DisplayReplicableValuesManager(object):
        pass


@registerRule
class TestClientDemoRules(Rule):
    category = DEMO_CATEGORY
    domain = CGF.DomainOption.DomainAll

    @registerManager(EntranceModifierManager)
    def registerEntranceModifier(self):
        return

    @registerManager(StateMachineActivatorManager)
    def registerStateActivator(self):
        return

    @registerManager(ModelSwapperManager)
    def registerModelSwapper(self):
        return

    @registerManager(DisplayReplicableValuesManager, domain=CGF.DomainOption.DomainClient)
    def registerDisplayReplicable(self):
        return

    @registerManager(EntranceSpawnerManager)
    def registerEntranceSpawner(self):
        return

    @registerManager(TestHealthMonitoringManager)
    def registerHealthMonitorManager(self):
        return