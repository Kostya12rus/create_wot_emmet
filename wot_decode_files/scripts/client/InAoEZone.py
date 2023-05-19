# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/InAoEZone.py
import BigWorld
from debug_utils import LOG_DEBUG_DEV
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from wotdecorators import noexcept

class InAoEZone(BigWorld.DynamicScriptComponent):
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(InAoEZone, self).__init__()
        if self.isVehicleInActiveZone():
            self.__guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.AOE_ZONE, self.inAoEZoneData)

    @noexcept
    def setSlice_inAoEZoneData(self, path, old):
        LOG_DEBUG_DEV('setSlice_inAoEZoneData in zone = ', self.isVehicleInActiveZone(), 'new', self.inAoEZoneData, 'path', path)
        self.__guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.AOE_ZONE, self.inAoEZoneData)

    def isVehicleInActiveZone(self):
        return len(self.inAoEZoneData) > 0