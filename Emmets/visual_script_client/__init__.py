# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/visual_script_client/__init__.py
from constants import IS_EDITOR
from visual_script.misc import ASPECT
from visual_script.registrar import VSBlockRegistrar
import arena_blocks, vehicle_blocks, scene_blocks, event_platform_blocks, triggers_blocks, hint_blocks, marker_blocks, player_blocks, sound_blocks, game_settings_blocks, hangar_blocks, battle_hud_block
from contexts.sound_notifications_context import SoundNotificationsContext
g_blockRegistrar = VSBlockRegistrar(ASPECT.CLIENT)
g_blockRegistrar.regBlocksFromModule(event_platform_blocks)
g_blockRegistrar.regBlocksFromModule(arena_blocks)
g_blockRegistrar.regBlocksFromModule(vehicle_blocks)
g_blockRegistrar.regBlocksFromModule(scene_blocks)
g_blockRegistrar.regBlocksFromModule(triggers_blocks)
g_blockRegistrar.regBlocksFromModule(hint_blocks)
g_blockRegistrar.regBlocksFromModule(marker_blocks)
g_blockRegistrar.regBlocksFromModule(player_blocks)
g_blockRegistrar.regBlocksFromModule(sound_blocks)
g_blockRegistrar.regBlocksFromModule(game_settings_blocks)
g_blockRegistrar.regBlocksFromModule(battle_hud_block)
g_blockRegistrar.regContext(SoundNotificationsContext)
if not IS_EDITOR:
    from visual_script_client import client_perk_blocks
    g_blockRegistrar.regBlocksFromModule(client_perk_blocks)
g_hangarBlockRegistrar = VSBlockRegistrar(ASPECT.HANGAR)
g_hangarBlockRegistrar.regBlocksFromModule(hangar_blocks)
g_hangarBlockRegistrar.regBlocksFromModule(hint_blocks)