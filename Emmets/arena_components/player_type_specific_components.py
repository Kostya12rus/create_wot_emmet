# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/arena_components/player_type_specific_components.py
from arena_components.epic_battle_player_data_component import EpicBattlePlayerDataComponent
from player_data_component import PlayerDataComponent
from advanced_chat_component import AdvancedChatComponent
from arena_component_system.epic_sector_warning_component import EpicSectorWarningComponent
from arena_component_system.arena_equipment_component import ArenaEquipmentComponent
from arena_component_system.overtime_component import OvertimeComponent

def getPlayerTypeSpecificComponentsForEpicRandom():
    return {'playerDataComponent': PlayerDataComponent}


def getPlayerTypeSpecificComponentsForEpicBattle():
    return {'playerDataComponent': EpicBattlePlayerDataComponent, 
       'sectorWarningComponent': EpicSectorWarningComponent, 
       'overtimeComponent': OvertimeComponent}


def getDefaultComponents():
    return {'arenaEquipmentComponent': ArenaEquipmentComponent, 
       'advancedChatComponent': AdvancedChatComponent}