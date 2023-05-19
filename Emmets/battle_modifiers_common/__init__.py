# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/battle_modifiers_common/__init__.py
import pkgutil
from ExtensionsManager import g_extensionsManager
from battle_modifiers import BattleParams, ModifiersContext, EXT_DATA_MODIFIERS_KEY
if 'battle_modifiers' in [ ext.name for ext in g_extensionsManager.activeExtensions ] and pkgutil.find_loader('battle_modifiers_ext'):
    from battle_modifiers_ext.battle_modifiers import BattleModifiers, getGlobalModifiers
    from battle_modifiers_ext import getModificationCache
else:
    from battle_modifiers import BattleModifiers, getGlobalModifiers, getModificationCache
__all__ = ('EXT_DATA_MODIFIERS_KEY', 'BattleParams', 'BattleModifiers', 'ModifiersContext',
           'getGlobalModifiers', 'getModificationCache')