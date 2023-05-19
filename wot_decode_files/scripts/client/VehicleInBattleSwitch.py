# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/VehicleInBattleSwitch.py
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS
from script_component.ScriptComponent import ScriptComponent

class VehicleInBattleSwitch(ScriptComponent):
    REQUIRED_BONUS_CAP = ARENA_BONUS_TYPE_CAPS.VEHICLE_IN_BATTLE_SELECTION