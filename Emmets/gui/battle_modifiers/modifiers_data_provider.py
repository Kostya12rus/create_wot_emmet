# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_modifiers/modifiers_data_provider.py
from typing import Tuple, Any, TYPE_CHECKING
from battle_modifiers.battle_modifiers import BattleModifiers
from battle_modifiers.battle_modifier_constants import GameplayImpact
if TYPE_CHECKING:
    from battle_modifiers.battle_modifiers import BattleModifier

class ModifiersDataProvider(object):
    __slots__ = ('__modifiers', '__domains', '__modifiersByDomain')

    def __init__(self, battleModifiersDescr=()):
        self.__modifiers = BattleModifiers(battleModifiersDescr)
        domains = tuple(str(modifier.param.clientData.domain) for _, modifier in self.__modifiers if not self.isHiddenModifier(modifier))
        self.__domains = tuple(domain for i, domain in enumerate(domains) if domain not in domains[:i])
        self.__modifiersByDomain = {domain:tuple(modifier for _, modifier in self.__modifiers if not self.isHiddenModifier(modifier) and modifier.param.clientData.domain == domain) for domain in self.__domains}

    @classmethod
    def isHiddenModifier(cls, mod):
        return mod.gameplayImpact == GameplayImpact.HIDDEN or mod.useType not in mod.param.clientData.useTypes

    def getDomains(self):
        return self.__domains

    def getDomainModifiers(self, domain):
        return self.__modifiersByDomain.get(domain, ())

    def getModifiers(self):
        return self.__modifiers