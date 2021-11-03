# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/genConsts/TOURNAMENT_ALIASES.py


class TOURNAMENT_ALIASES(object):
    TOURNAMENT_BATTLE_ROOM_WINDOW_ALIAS = 'TournamentRoomWindow'
    TOURNAMENT_BATTLE_ROOM_WINDOW_UI = 'fortBattleRoomWindow.swf'
    TOURNAMENT_BATTLE_ROOM_LIST_VIEW_UI = 'StrongholdListViewUI'
    TOURNAMENT_BATTLE_ROOM_LIST_VIEW_PY = 'tournament/battleRoom/list'
    TOURNAMENT_BATTLE_ROOM_VIEW_UI = 'FortClanBattleRoomUI'
    TOURNAMENT_BATTLE_ROOM_VIEW_PY = 'forttifications/battleRoom/tournamentBattleRoom'
    FLASH_ALIASES = [TOURNAMENT_BATTLE_ROOM_LIST_VIEW_UI, TOURNAMENT_BATTLE_ROOM_VIEW_UI]
    PYTHON_ALIASES = [TOURNAMENT_BATTLE_ROOM_LIST_VIEW_PY, TOURNAMENT_BATTLE_ROOM_VIEW_PY]
    STATE_TROWEL = 0
    STATE_FOUNDATION = 1
    STATE_FOUNDATION_DEF = 2
    STATE_BUILDING = 3
    STATES = [STATE_TROWEL, STATE_FOUNDATION, STATE_FOUNDATION_DEF, STATE_BUILDING]