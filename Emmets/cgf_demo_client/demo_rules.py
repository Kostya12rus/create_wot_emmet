# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_demo_client/demo_rules.py
from cgf_demo.demo_category import DEMO_CATEGORY
from cgf_demo_client.test_hierarchy_modificator import ModelSwapperManager
from cgf_demo_client.test_state_machine_trigger import StateMachineActivatorManager
from cgf_demo_client.test_triggers import EntranceModifierManager
from cgf_script.managers_registrator import Rule, registerManager

class TestClientDemoRules(Rule):
    category = DEMO_CATEGORY

    @registerManager(EntranceModifierManager)
    def registerEntranceModifier(self):
        return

    @registerManager(StateMachineActivatorManager)
    def registerStateActivator(self):
        return

    @registerManager(ModelSwapperManager)
    def registerModelSwapper(self):
        return