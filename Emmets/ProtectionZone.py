# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/ProtectionZone.py
import BigWorld, Math
from debug_utils import LOG_DEBUG

class ProtectionZone(BigWorld.Entity):

    def __init__(self):
        super(ProtectionZone, self).__init__(self)
        self.__lowerLeft = Math.Vector2(0, 0)
        self.__upperRight = Math.Vector2(0, 0)

    def onEnterWorld(self, prereqs):
        LOG_DEBUG('ProtectionZone added ', self.zoneID)
        self.__lowerLeft = Math.Vector2(self.position.x - self.lengthX * 0.5, self.position.z - self.lengthZ * 0.5)
        self.__upperRight = Math.Vector2(self.position.x + self.lengthX * 0.5, self.position.z + self.lengthZ * 0.5)
        protectionZoneComponent = BigWorld.player().arena.componentSystem.protectionZoneComponent
        if protectionZoneComponent is not None:
            protectionZoneComponent.addProtectionZone(self)
            if self.isActive:
                protectionZoneComponent.setProtectionZoneActive(self.zoneID, self.isActive)
        return

    def onLeaveWorld(self):
        protectionZoneComponent = BigWorld.player().arena.componentSystem.protectionZoneComponent
        if protectionZoneComponent is not None:
            protectionZoneComponent.removeProtectionZone(self)
        return

    def set_isActive(self, oldValue):
        LOG_DEBUG('ProtectionZone active: ' + str(self.isActive))
        protectionZoneComponent = BigWorld.player().arena.componentSystem.protectionZoneComponent
        if protectionZoneComponent is not None:
            protectionZoneComponent.setProtectionZoneActive(self.zoneID, self.isActive)
        return

    @property
    def bound(self):
        return (self.__lowerLeft, self.__upperRight)