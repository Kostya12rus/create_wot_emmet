# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/limited_ui/lui_tutorial_hints.py
from gui.limited_ui.lui_rules_storage import LuiRules
from helpers import dependency
from skeletons.gui.game_control import ILimitedUIController
_ALIAS_TO_RULE_ID = {'blueprintsButton': LuiRules.BLUEPRINTS_BUTTON, 
   'DogTagHangarHint': LuiRules.DOG_TAG_HINT, 
   'PersonalReservesHangarHint': LuiRules.PR_HANGAR_HINT, 
   'sessionStats': LuiRules.SESSION_STATS, 
   'ModernizedSetupTabHint': LuiRules.MODERNIZE_SETUP_HINT, 
   'ModeSelectorWidgetsBtnHint': LuiRules.MODE_SELECTOR_WIDGET_BTN_HINT, 
   'AmmunitionPanelHintZoneHint': LuiRules.AP_ZONE_HINT}

class LimitedUIHintChecker(object):

    def check(self, aliasId):
        limitedUIController = dependency.instance(ILimitedUIController)
        ruleID = _ALIAS_TO_RULE_ID.get(aliasId)
        return ruleID is None or limitedUIController.isRuleCompleted(ruleID)