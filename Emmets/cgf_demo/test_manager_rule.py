# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/cgf_demo/test_manager_rule.py
from cgf_script.managers_registrator import Rule, registerManager
from cgf_demo.demo_category import DEMO_CATEGORY
from cgf_demo.test_bridge import TestBridgeManager
from cgf_demo.test_movers import TestAxisRotatorManager
from cgf_demo.test_triggers import TestTriggersManager, TestComponentCreationManager
import logging
_logger = logging.getLogger(__name__)

class TestMapArenaManagerRule(Rule):
    category = DEMO_CATEGORY

    def __init__(self):
        super(TestMapArenaManagerRule, self).__init__()
        _logger.debug('TestMapArenaManagerRule Created')

    @registerManager(TestBridgeManager)
    def registerBridge(self):
        _logger.debug('TestBridgeManager Registrator')
        return

    @registerManager(TestAxisRotatorManager)
    def registerAxisRotator(self):
        _logger.debug('TestAxisRotatorManager Registrator')
        return

    @registerManager(TestTriggersManager)
    def registerTriggerManager(self):
        _logger.debug('TestTriggersManager Registrator')
        return

    @registerManager(TestComponentCreationManager)
    def registerTestComponentCreationManager(self):
        _logger.debug('TestComponentCreationManager Registrator')
        return