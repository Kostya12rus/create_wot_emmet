# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/genConsts/GAME_MESSAGES_CONSTS.py


class GAME_MESSAGES_CONSTS(object):
    WIN = 'win'
    DEFEAT = 'lose'
    DRAW = 'tie'
    TIME_REMAINING_POSITIVE = 'timeRemainingPositive'
    TIME_REMAINING = 'timeRemaining'
    OVERTIME = 'overTime'
    BASE_CAPTURED_POSITIVE = 'baseCapturedPositive'
    BASE_CAPTURED = 'baseCaptured'
    BASE_CONTESTED_POSITIVE = 'baseContestedPositive'
    BASE_CONTESTED = 'baseContested'
    RANK_UP = 'rankUp'
    OBJECTIVE_DESTROYED_POSITIVE = 'objectiveDestroyedPositive'
    OBJECTIVE_DESTROYED = 'objectiveDestroyed'
    DESTROY_OBJECTIVE = 'destroyObjective'
    DEFEND_OBJECTIVE = 'defendObjective'
    CAPTURE_BASE = 'captureBase'
    DEFEND_BASE = 'defendBase'
    RETREAT = 'retreat'
    OBJECTIVE_UNDER_ATTACK_POSITIVE = 'objectiveUnderAttackPositive'
    OBJECTIVE_UNDER_ATTACK = 'objectiveUnderAttack'
    GENERAL_RANK_REACHED = 'generalRankReached'
    UNLOCK_TANK_LEVEL = 'unlockTankLevel'
    HQ_BATTLE_STARTED = 'hqBattleStarted'
    HQ_BATTLE_STARTED_POSITIVE = 'hqBattleStartedPositive'
    RETREAT_SUCCESSFUL = 'retreatSuccessful'
    WITH_ADD_TIME = 'withAddTime'
    WITH_UNLOCK = 'withUnlock'
    WITH_EVENT = 'withEvent'
    WITH_HIDE = 'withHide'
    GAME_MESSAGE_PRIORITY_HIGH = 0
    GAME_MESSAGE_PRIORITY_LOW = 1
    GAME_MESSAGE_PRIORITY_DEFAULT = 2
    GAME_MESSAGE_PRIORITY_END_GAME = 3
    DEFAULT_MESSAGE_LENGTH = 5000