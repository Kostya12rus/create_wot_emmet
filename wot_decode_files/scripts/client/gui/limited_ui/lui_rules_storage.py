# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/limited_ui/lui_rules_storage.py
from collections import namedtuple
import enum, typing
from expressions import parseExpression
from ids_generators import SequenceIDGenerator
if typing.TYPE_CHECKING:
    from typing import Optional, Dict, Set, List, Tuple

class LuiRules(enum.Enum):
    LOBBY_HEADER_COUNTERS_STORE = 'store'
    LOBBY_HEADER_COUNTERS_PROFILE = 'profile'
    PROFILE_HOF = 'profileHof'
    PROFILE_TECHNIQUE_PAGE = 'profileTechniquePage'
    SESSION_STATS = 'sessionStats'
    BLUEPRINTS_BUTTON = 'blueprintsButton'
    LOBBY_HEADER_COUNTERS_MISSIONS = 'missions'
    MISSIONS_MARATHON_VIEW = 'MissionsMarathonView'
    LOBBY_HEADER_COUNTERS_PM_OPERATIONS = 'PersonalMissionOperations'
    REFERRAL_BTN_COUNTER = 'referralButtonCounter'
    AP_ZONE_HINT = 'AmmunitionPanelHintZoneHint'
    AP_BATTLE_ABILITIES_HINT = 'AmmunitionPanelBattleAbilitiesHint'
    C7N_PROGRESSION_HINT = 'CustomizationProgressionViewHint'
    TECH_TREE_EVENTS = 'TechTreeEvent'
    DOG_TAG_HINT = 'DogTagHangarHint'
    MODE_SELECTOR_WIDGET_BTN_HINT = 'ModeSelectorWidgetsBtnHint'
    PR_HANGAR_HINT = 'PersonalReservesHangarHint'
    MODERNIZE_SETUP_HINT = 'ModernizedSetupTabHint'
    OFFER_BANNER_WINDOW = 'OfferBannerWindow'
    COMP7_ENTRY_POINT = 'Comp7EntryPoint'
    BP_ENTRY = 'BattlePassEntry'
    PROGRESSIVE_ITEMS_REWARD = 'ProgressiveItemsReward'
    DAILY_MISSIONS = 'DailyMissions'
    CRAFT_MACHINE_ENTRY_POINT = 'CraftMachineEntryPoint'
    MAPBOX_ENTRY_POINT = 'MapboxEntryPoint'
    EPIC_BATTLES_ENTRY_POINT = 'EpicBattlesEntryPoint'
    BATTLE_MISSIONS = 'BattleMissions'
    HERO_TANK = 'HeroTank'
    BM_FLAG = 'BattleMattersFlag'
    PERSONAL_MISSIONS = 'PersonalMissions'
    SYS_MSG_COLLECTION_START_BP = 'sysMsgCollectionStartBattlePass'
    LOBBY_HEADER_COUNTERS_STORAGE = 'storage'
    PR_HANGAR_BUTTON = 'PersonalReservesHangarButton'
    STRONGHOLD_ENTRY_POINT = 'StrongholdEntryPoint'
    BR_ENTRY_POINT = 'BREntryPoint'


class _LimitedUIRule(namedtuple('_LimitedUIRule', ('idx', 'expression', 'tokens', 'message'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(idx=0, expression=None, tokens=set(), message=None)
        dataToUpdate = {k: v for k, v in kwargs.iteritems() if k in cls._fields}
        defaults.update(dataToUpdate)
        return super(_LimitedUIRule, cls).__new__(cls, **defaults)


class _LimitedUIRules(object):

    def __init__(self, rules):
        super(_LimitedUIRules, self).__init__()
        self.__rules = rules

    def getRule(self, ruleID):
        return self.__rules.get(ruleID, None)

    def getRulesIDs(self):
        return set(self.__rules.keys())

    def hasRule(self, ruleID):
        return ruleID in self.__rules

    def getTokens(self, ruleID):
        if self.hasRule(ruleID):
            return self.getRule(ruleID).tokens
        return set()

    def getSysMessage(self, ruleID):
        if self.hasRule(ruleID):
            return self.getRule(ruleID).message

    def clear(self):
        self.__rules.clear()


class RulesStorageMaker(object):

    @classmethod
    def makeStorage(cls, rulesData):
        data = dict()
        idGen = SequenceIDGenerator(lowBound=-1)
        for ruleID, expressionStr, message in rulesData:
            expression, tokens = parseExpression(expressionStr)
            data[ruleID] = {'idx': idGen.next(), 
               'expressionStr': expressionStr, 
               'expression': expression, 
               'tokens': tokens, 
               'message': message}

        rulesIDs = set(data.keys())
        for ruleID, item in data.items():
            cls.__normalizeRuleItem(data, rulesIDs, item)

        rules = {LuiRules(ruleID): _LimitedUIRule(**value) for ruleID, value in data.items()}
        return _LimitedUIRules(rules)

    @classmethod
    def __normalizeRuleItem(cls, data, rulesIDs, item):
        tokens = item['tokens']
        expressionStr = item['expressionStr']
        dependencies = tokens & rulesIDs
        if dependencies:
            while dependencies:
                dependency = dependencies.pop()
                dependsItem = data[dependency]
                dependencyExpression = cls.__normalizeRuleItem(data, rulesIDs, dependsItem)
                expressionStr = expressionStr.replace(dependency, ('({})').format(dependencyExpression))

            expression, tokens = parseExpression(expressionStr)
            item['expressionStr'] = expressionStr
            item['expression'] = expression
            item['tokens'] = tokens
        return expressionStr