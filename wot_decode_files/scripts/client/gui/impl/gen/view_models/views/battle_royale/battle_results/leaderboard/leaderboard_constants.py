# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle_royale/battle_results/leaderboard/leaderboard_constants.py
from frameworks.wulf import ViewModel

class LeaderboardConstants(ViewModel):
    __slots__ = ()
    LIST_TYPE_BR_SOLO = 'listBrSolo'
    LIST_TYPE_BR_PLATOON = 'listBrPlatoon'
    ROW_TYPE_BR_PLAYER = 'rowBrPlayer'
    ROW_TYPE_BR_PLATOON = 'rowBrPlatoon'
    ROW_TYPE_BR_ENEMY = 'rowBrEnemy'

    def __init__(self, properties=0, commands=0):
        super(LeaderboardConstants, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(LeaderboardConstants, self)._initialize()