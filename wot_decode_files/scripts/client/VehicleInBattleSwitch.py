# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/VehicleInBattleSwitch.py
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS
from script_component.ScriptComponent import ScriptComponent

class VehicleInBattleSwitch(ScriptComponent):
    REQUIRED_BONUS_CAP = ARENA_BONUS_TYPE_CAPS.VEHICLE_IN_BATTLE_SELECTION