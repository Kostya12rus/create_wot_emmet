# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/items/tournament_items.py
from collections import namedtuple
from gui.prb_control.items.stronghold_items import StrongholdSettings

def isEnemyBattleIndex(index):
    return index >= 4


class TournamentSettings(StrongholdSettings):

    def isTournamentUnitFreezed(self):
        return super(TournamentSettings, self).isStrongholdUnitFreezed()


TournamentUnitStats = namedtuple('UnitStats', ('readyCount', 'occupiedSlotsCount',
                                               'openedSlotsCount', 'freeSlotsCount',
                                               'curTotalLevel', 'levelsSeq', 'clanMembersInRoster',
                                               'legionariesInRoster', 'playersMatchingSlotsCount'))
TournamentUnitStats.__new__.__defaults__ = (
 0, 0, 0, 0, 0, (), 0, 0, 0)