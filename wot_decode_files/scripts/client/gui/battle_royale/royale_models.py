# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_royale/royale_models.py
from collections import namedtuple
from season_common import GameSeason

class BattleRoyaleCycle(namedtuple('BattleRoyaleCycle', 'ID, status, startDate, endDate, ordinalNumber, announceOnly')):

    def __cmp__(self, other):
        return cmp(self.ID, other.ID)

    def getEpicCycleNumber(self):
        return self.ordinalNumber


class BattleRoyaleSeason(GameSeason):

    def _buildCycle(self, idx, status, start, end, number, announceOnly):
        return BattleRoyaleCycle(idx, status, start, end, number, announceOnly)