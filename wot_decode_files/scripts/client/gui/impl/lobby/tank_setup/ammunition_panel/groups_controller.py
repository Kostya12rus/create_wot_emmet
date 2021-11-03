# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/ammunition_panel/groups_controller.py
from constants import QUEUE_TYPE, PREBATTLE_TYPE
from gui.prb_control import prbDispatcherProperty
from gui.impl.common.ammunition_panel.ammunition_groups_controller import AmmunitionGroupsController, FRONTLINE_GROUPS, RANDOM_GROUPS, HALLOWEEN_GROUPS
from helpers import dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController

class HangarAmmunitionGroupsController(AmmunitionGroupsController):
    __slots__ = ()
    __epicMetaGameCtrl = dependency.descriptor(IEpicBattleMetaGameController)

    @prbDispatcherProperty
    def prbDispatcher(self):
        return

    def _getGroups(self):
        if self._vehicle is None:
            return []
        else:
            if self.prbDispatcher is not None and (self.prbDispatcher.getFunctionalState().isInPreQueue(QUEUE_TYPE.EPIC) or self.prbDispatcher.getFunctionalState().isInUnit(PREBATTLE_TYPE.EPIC)) and self._vehicle.level in self.__epicMetaGameCtrl.getValidVehicleLevels():
                return FRONTLINE_GROUPS
            if self.prbDispatcher is not None and (self.prbDispatcher.getFunctionalState().isInPreQueue(QUEUE_TYPE.EVENT_BATTLES) or self.prbDispatcher.getFunctionalState().isInUnit(PREBATTLE_TYPE.EVENT)) and self._vehicle.level in self.__epicMetaGameCtrl.getValidVehicleLevels():
                return HALLOWEEN_GROUPS
            return RANDOM_GROUPS