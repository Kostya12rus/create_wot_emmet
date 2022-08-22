# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client_common/arena_component_system/assembler_helper.py
from battleground.airdrops import AirdropsComponent
from battleground.berserker_effect import BerserkerEffectComponent
from constants import ARENA_BONUS_TYPE
from arena_component_system.destructible_entity_component import DestructibleEntitiesComponent
from arena_component_system.sector_base_arena_component import SectorBaseArenaComponent
from arena_component_system.sectors_arena_component import SectorsArenaComponent
from arena_component_system.step_repair_point_component import StepRepairPointComponent
from arena_component_system.epic_random_battle_component_assembler import EpicRandomBattleComponentAssembler
from arena_component_system.epic_battle_component_assembler import EpicBattleComponentAssembler
from arena_component_system.protection_zone_component import ProtectionZoneComponent
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS
from arena_components.battle_royale_component import BattleRoyaleComponent
COMPONENT_ASSEMBLER = {ARENA_BONUS_TYPE.EPIC_RANDOM: EpicRandomBattleComponentAssembler, 
   ARENA_BONUS_TYPE.EPIC_RANDOM_TRAINING: EpicRandomBattleComponentAssembler, 
   ARENA_BONUS_TYPE.EPIC_BATTLE: EpicBattleComponentAssembler, 
   ARENA_BONUS_TYPE.EPIC_BATTLE_TRAINING: EpicBattleComponentAssembler}
ARENA_BONUS_TYPE_CAP_COMPONENTS = {'sectorBaseComponent': (
                         ARENA_BONUS_TYPE_CAPS.SECTOR_MECHANICS, SectorBaseArenaComponent), 
   'sectorComponent': (
                     ARENA_BONUS_TYPE_CAPS.SECTOR_MECHANICS, SectorsArenaComponent), 
   'destructibleEntityComponent': (
                                 ARENA_BONUS_TYPE_CAPS.DESTRUCTIBLE_ENTITIES, DestructibleEntitiesComponent), 
   'stepRepairPointComponent': (
                              ARENA_BONUS_TYPE_CAPS.STEP_REPAIR_MECHANIC, StepRepairPointComponent), 
   'protectionZoneComponent': (
                             ARENA_BONUS_TYPE_CAPS.PROTECTION_ZONE, ProtectionZoneComponent), 
   'airDropComponent': (
                      ARENA_BONUS_TYPE_CAPS.LOOT_DROP, AirdropsComponent), 
   'battleRoyaleComponent': (
                           ARENA_BONUS_TYPE_CAPS.BATTLEROYALE, BattleRoyaleComponent), 
   'berserkerEffectComponent': (
                              ARENA_BONUS_TYPE_CAPS.BATTLEROYALE, BerserkerEffectComponent)}