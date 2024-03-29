# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/epic/pre_queue/permissions.py
from gui.prb_control.entities.base.pre_queue.permissions import PreQueuePermissions
from helpers import time_utils, dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController

class EpicPermissions(PreQueuePermissions):
    __epicCtrl = dependency.descriptor(IEpicBattleMetaGameController)

    def canCreateSquad(self):
        currentSeason = self.__epicCtrl.getCurrentSeason()
        if currentSeason:
            if currentSeason.hasActiveCycle(time_utils.getCurrentLocalServerTimestamp()):
                return True
        return False