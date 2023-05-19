# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/TeamInfo.py
import BigWorld
from debug_utils import LOG_DEBUG_DEV
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class TeamInfo(BigWorld.Entity):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def onCombatEquipmentUsed(self, vehicleID, equipmentID):
        self.__sessionProvider.shared.equipments.onCombatEquipmentUsed(vehicleID, equipmentID)

    def onEnterWorld(self, prereqs):
        LOG_DEBUG_DEV(('[TeamInfo] onEnterWorld: team = {}').format(self.teamID))
        BigWorld.player().arena.registerTeamInfo(self)

    def onLeaveWorld(self):
        LOG_DEBUG_DEV(('[TeamInfo] onLeaveWorld: team = {}').format(self.teamID))
        BigWorld.player().arena.unregisterTeamInfo(self)

    def onDynamicComponentCreated(self, component):
        LOG_DEBUG_DEV('Component created', component)