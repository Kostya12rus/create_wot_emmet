# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/avatar_helpers/__init__.py
import BigWorld
from shared_utils.avatar_helpers import VehicleTelemetry

def getAvatarDatabaseID():
    dbID = 0
    player = BigWorld.player()
    arena = getattr(player, 'arena', None)
    if arena is not None:
        vehID = getattr(player, 'playerVehicleID', None)
        if vehID is not None and vehID in arena.vehicles:
            dbID = arena.vehicles[vehID]['accountDBID']
    return dbID


def getAvatarSessionID():
    player = BigWorld.player()
    avatarSessionID = getattr(player, 'sessionID', '')
    return avatarSessionID


def getBestShotResultSound(currBest, newSoundName, otherData):
    newSoundPriority = _shotResultSoundPriorities[newSoundName]
    if currBest is None:
        return (newSoundName, otherData, newSoundPriority)
    else:
        if newSoundPriority > currBest[2]:
            return (newSoundName, otherData, newSoundPriority)
        return currBest


_shotResultSoundPriorities = {'enemy_hp_damaged_by_projectile_and_gun_damaged_by_player': 12, 
   'enemy_hp_damaged_by_projectile_and_chassis_damaged_by_player': 11, 
   'enemy_hp_damaged_by_projectile_by_player': 10, 
   'enemy_hp_damaged_by_explosion_at_direct_hit_by_player': 9, 
   'enemy_hp_damaged_by_near_explosion_by_player': 8, 
   'enemy_no_hp_damage_at_attempt_and_gun_damaged_by_player': 7, 
   'enemy_no_hp_damage_at_no_attempt_and_gun_damaged_by_player': 6, 
   'enemy_no_hp_damage_at_attempt_and_chassis_damaged_by_player': 5, 
   'enemy_no_hp_damage_at_no_attempt_and_chassis_damaged_by_player': 4, 
   'enemy_no_piercing_by_player': 3, 
   'enemy_no_hp_damage_at_attempt_by_player': 3, 
   'enemy_no_hp_damage_at_no_attempt_by_player': 2, 
   'enemy_no_hp_damage_by_near_explosion_by_player': 1, 
   'enemy_ricochet_by_player': 0}