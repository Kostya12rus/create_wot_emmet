# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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