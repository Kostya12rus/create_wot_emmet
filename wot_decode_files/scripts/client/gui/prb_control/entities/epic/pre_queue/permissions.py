# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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