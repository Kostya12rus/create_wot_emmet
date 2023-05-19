# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/ui_spam/ui_spam_config.py
import ResMgr

class UISpamConfig(object):

    def __init__(self, aliases, rules):
        super(UISpamConfig, self).__init__()
        self._aliases = aliases
        self._rules = rules

    def getRule(self, ruleId):
        return self._rules.get(ruleId, {})

    def getRuleIdForAlias(self, aliasId):
        return self._aliases.get(aliasId, '')


class UISpamConfigReader(object):

    @staticmethod
    def readXml(xmlPath):
        section = ResMgr.openSection(xmlPath)
        aliasesData = dict()
        aliasesSection = section['aliases']
        for aliasSection in aliasesSection.values():
            aliasId = aliasSection.readString('id', '')
            aliasesData[aliasId] = aliasSection.readString('rule', '')

        rulesData = dict()
        rulesSection = section['rules']
        for ruleSection in rulesSection.values():
            ruleId = ruleSection.readString('id', '')
            conditions = {name: value.asInt for name, value in ruleSection['condition'].items()}
            rulesData[ruleId] = conditions

        ResMgr.purge(xmlPath)
        return UISpamConfig(aliasesData, rulesData)