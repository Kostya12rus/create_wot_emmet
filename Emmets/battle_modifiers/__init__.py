# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/battle_modifiers/__init__.py
import ResMgr, battle_params, vehicle_modifications
from battle_modifiers import BattleModifiers
from battle_modifier_constants import BATTLE_MODIFIERS_DIR, BATTLE_MODIFIERS_XML
from constants import IS_DEVELOPMENT, IS_BASEAPP
from typing import Optional
from debug_utils import LOG_DEBUG
g_cache = None

def init():
    battle_params.init()
    vehicle_modifications.init()
    initGlobalBattleModifiers()


def initGlobalBattleModifiers():
    global g_cache
    if not IS_DEVELOPMENT or not IS_BASEAPP:
        return
    modifiersSection = _readModifiersSection()
    if modifiersSection:
        g_cache = BattleModifiers(modifiersSection)
        LOG_DEBUG(('[BattleModifiers] Use global battle modifiers: {}').format(g_cache))


def _readModifiersSection():
    config = ResMgr.openSection(BATTLE_MODIFIERS_DIR + BATTLE_MODIFIERS_XML)
    if config is None:
        return
    else:
        if config.has_key('config') and config['config'].asString:
            return ResMgr.openSection(BATTLE_MODIFIERS_DIR + config['config'].asString)
        return config['modifiers']