# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/battle_royale_tournament/pre_queue/permissions.py
from gui.prb_control.entities.base.pre_queue.permissions import PreQueuePermissions

class BattleRoyaleTournamentPermissions(PreQueuePermissions):

    def canCreateSquad(self):
        return False