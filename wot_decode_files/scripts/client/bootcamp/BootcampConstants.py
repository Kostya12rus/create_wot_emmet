# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/bootcamp/BootcampConstants.py
CAMERA_START_DISTANCE = 12

class UI_STATE(object):
    INIT = 1
    START = 2
    UPDATE = 3
    STOP = 4


class BATTLE_STATS_TOOLTIPS:
    DESTROYED = 'destroyed'
    DAMAGE = 'damage'
    BLOCKED = 'blocked'
    DETECTED = 'detected'
    ASSISTED = 'assisted'


BATTLE_STATS_RESULT_FIELDS = {BATTLE_STATS_TOOLTIPS.DESTROYED: 'kills', 
   BATTLE_STATS_TOOLTIPS.DAMAGE: 'damageDealt', 
   BATTLE_STATS_TOOLTIPS.BLOCKED: 'damageBlockedByArmor', 
   BATTLE_STATS_TOOLTIPS.DETECTED: 'spotted', 
   BATTLE_STATS_TOOLTIPS.ASSISTED: 'damageAssisted'}
BATTLE_STATS_ICONS = {BATTLE_STATS_TOOLTIPS.DESTROYED: 'statIconDestroyed', 
   BATTLE_STATS_TOOLTIPS.DAMAGE: 'statIconDamage', 
   BATTLE_STATS_TOOLTIPS.BLOCKED: 'statIconBlocked', 
   BATTLE_STATS_TOOLTIPS.DETECTED: 'statIconDetected', 
   BATTLE_STATS_TOOLTIPS.ASSISTED: 'statIconAssisted'}
CONSUMABLE_ERROR_MESSAGES = ('repairkitAllDevicesAreNotDamaged', 'repairkitDeviceIsNotDamaged',
                             'medkitAllTankmenAreSafe', 'medkitTankmanIsSafe', 'extinguisherDoesNotActivated')

class HINT_TYPE:
    HINT_MOVE = 0
    HINT_MOVE_TURRET = 1
    HINT_SHOOT = 2
    HINT_ADVANCED_SNIPER = 3
    HINT_AIM = 4
    HINT_SNIPER = 5
    HINT_WEAK_POINTS = 6
    HINT_MESSAGE_AVOID = 7
    HINT_MESSAGE_PLAYER_SPOTTED = 8
    HINT_SECTOR_CLEAR = 9
    HINT_START_NARRATIVE = 10
    HINT_MESSAGE_CAPTURE_THE_BASE = 11
    HINT_MESSAGE_RESET_PROGRESS = 12
    HINT_REPAIR_TRACK = 13
    HINT_HEAL_CREW = 14
    HINT_USE_EXTINGUISHER = 15
    HINT_SHOOT_ALLY = 16
    HINT_PLAYER_DETECT_ENEMIES = 17
    HINT_EXIT_GAME_AREA = 18
    HINT_MESSAGE_ENEMY_CAN_HIDE = 19
    HINT_MESSAGE_SNEAK = 20
    HINT_SNIPER_ON_DISTANCE = 21
    HINT_ROTATE_LOBBY = 22
    HINT_TARGET_LOCK = 23
    HINT_WAIT_RELOAD = 24
    HINT_NO_MOVE = 25
    HINT_NO_MOVE_TURRET = 26
    HINT_SHOT_WHILE_MOVING = 27
    HINT_MOVE_TO_MARKER = 28
    HINT_SECONDARY_SNIPER = 29
    HINT_USELESS_CONSUMABLE = 30
    HINT_LOW_HP = 31
    HINT_UNLOCK_TARGET = 32
    HINT_B3_YOU_ARE_DETECTED = 33
    HINT_B3_FALL_BACK = 34
    HINT_B3_FOLIAGE = 35
    HINT_B3_DO_CAPTURE = 36
    HINT_B3_CAPTURE_IN_PROGRESS = 37
    HINT_B3_ENEMIES_HIDDEN = 38
    HINT_B3_CAPTURE_RESET = 39
    HINT_B3_FOLIAGE2 = 40
    HINT_B3_FLANK = 41
    HINT_B3_CAPTURE_TOGETHER = 42
    HINT_SNIPER_LEVEL0 = 43
    HINT_CUSTOM = 44
    HINTS_B3_CAPTURE = (
     HINT_B3_DO_CAPTURE, HINT_B3_CAPTURE_IN_PROGRESS, HINT_B3_CAPTURE_RESET,
     HINT_B3_CAPTURE_TOGETHER)
    HINTS_B3_DETECTED = (
     HINT_B3_YOU_ARE_DETECTED,)
    BATTLE_HINTS = (
     HINT_MOVE, HINT_MOVE_TURRET, HINT_SHOOT, HINT_SNIPER, HINT_SNIPER_LEVEL0,
     HINT_ADVANCED_SNIPER, HINT_MESSAGE_AVOID, HINT_MESSAGE_PLAYER_SPOTTED,
     HINT_MESSAGE_SNEAK, HINT_MESSAGE_ENEMY_CAN_HIDE, HINT_MESSAGE_CAPTURE_THE_BASE,
     HINT_MESSAGE_RESET_PROGRESS, HINT_WEAK_POINTS,
     HINT_REPAIR_TRACK, HINT_USE_EXTINGUISHER, HINT_HEAL_CREW, HINT_AIM, HINT_EXIT_GAME_AREA,
     HINT_SECTOR_CLEAR, HINT_PLAYER_DETECT_ENEMIES, HINT_SNIPER_ON_DISTANCE,
     HINT_TARGET_LOCK, HINT_WAIT_RELOAD, HINT_NO_MOVE, HINT_NO_MOVE_TURRET,
     HINT_SHOT_WHILE_MOVING, HINT_MOVE_TO_MARKER, HINT_SECONDARY_SNIPER,
     HINT_USELESS_CONSUMABLE, HINT_CUSTOM, HINT_LOW_HP, HINT_UNLOCK_TARGET,
     HINT_B3_YOU_ARE_DETECTED, HINT_B3_FALL_BACK, HINT_B3_FOLIAGE, HINT_B3_DO_CAPTURE,
     HINT_B3_CAPTURE_IN_PROGRESS, HINT_B3_ENEMIES_HIDDEN, HINT_B3_CAPTURE_RESET, HINT_B3_FOLIAGE2,
     HINT_B3_FLANK, HINT_B3_CAPTURE_TOGETHER)
    SECONDARY_HINTS = (
     HINT_WAIT_RELOAD, HINT_EXIT_GAME_AREA, HINT_AIM, HINT_SECONDARY_SNIPER,
     HINT_NO_MOVE, HINT_NO_MOVE_TURRET, HINT_SHOT_WHILE_MOVING, HINT_MOVE_TO_MARKER,
     HINT_USELESS_CONSUMABLE, HINT_LOW_HP, HINT_UNLOCK_TARGET)


HINT_NAMES = ('hintMove', 'hintMoveTurret', 'hintShoot', 'hintAdvancedSniper', 'hintAim',
              'hintSniper', 'hintWeakPoints', 'hintMessageAvoid', 'hintPlayerSpotted',
              'hintSectorClear', 'hintStartNarrative', 'hintCaptureTheBase', 'hintResetProgress',
              'hintRepairTrack', 'hintHealCrew', 'hintUseExtinguisher', 'hintAllyShoot',
              'hintPlayerDetectEnemies', 'hintExitGameArea', 'hintEnemyCanHide',
              'hintSneak', 'hintSniperOnDistance', 'hintRotateLobby', 'hintTargetLock',
              'hintWaitReload', 'hintNoMove', 'hintNoMoveTurret', 'hintShootWhileMoving',
              'hintMoveToMarker', 'hintSecondarySniper', 'hintUselessConsumable',
              'hintLowHP', 'hintTargetUnLock', 'hintB3PlayerDetected', 'hintB3FallBack',
              'hintB3Foliage', 'hintB3DoCapture', 'hintB3CaptureInProgress', 'hintB3EnemiesHidden',
              'hintB3CaptureReset', 'hintB3Foliage2', 'hintB3Flank', 'hintB3CaptureTogether',
              'hintSniperLevel0', 'hintCustom')

class BOOTCAMP_BATTLE_RESULT_MESSAGE:
    DRAW = 0
    VICTORY = 1
    DEFEAT = 2
    FAILURE = 3