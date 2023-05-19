# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/training/legacy/permissions.py
from constants import PREBATTLE_ROLE
from gui.prb_control.entities.base.legacy.permissions import LegacyPermissions, ILegacyPermissions

class TrainingPermissions(LegacyPermissions):

    def canChangeVehicle(self):
        return True

    def canCreateSquad(self):
        return False

    @classmethod
    def isCreator(cls, roles):
        return roles == PREBATTLE_ROLE.TRAINING_CREATOR

    def canChangeSetting(self):
        return self.canChangeComment() or self.canChangeArena() or self.canMakeOpenedClosed()

    def canStartBattle(self):
        return self.canSetTeamState(1) and self.canSetTeamState(2)


class TrainingIntroPermissions(ILegacyPermissions):

    def canCreateSquad(self):
        return False