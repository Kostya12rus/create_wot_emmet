# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client_common/arena_component_system/protection_zone_component.py
from client_arena_component_system import ClientArenaComponent
import Event

class ProtectionZoneComponent(ClientArenaComponent):
    protectionZones = property((lambda self: self.__protectionZones))

    def __init__(self, componentSystem):
        ClientArenaComponent.__init__(self, componentSystem)
        self.__protectionZones = {}
        self.__isPlayerInZone = {}
        self.onProtectionZoneAdded = Event.Event(self._eventManager)
        self.onProtectionZoneActive = Event.Event(self._eventManager)
        self.onPlayerInProtectedZoneAction = Event.Event(self._eventManager)

    def addProtectionZone(self, protZone):
        self.__protectionZones[protZone.zoneID] = protZone
        self.__isPlayerInZone[protZone.zoneID] = False
        self.onProtectionZoneAdded(protZone.zoneID, protZone.position, protZone.bound)

    def setProtectionZoneActive(self, zoneID, isActive):
        self.onProtectionZoneActive(zoneID, isActive)

    def removeProtectionZone(self, protZone):
        if protZone in self.__protectionZones:
            del self.__protectionZones[protZone.zoneID]
        self.__isPlayerInZone[protZone.zoneID] = False

    def getProtectionZoneById(self, zoneID):
        if zoneID in self.__protectionZones:
            return self.__protectionZones[zoneID]
        else:
            return

    def getOwningTeamForZone(self, zoneID):
        zone = self.getProtectionZoneById(zoneID)
        if zone is not None:
            return zone.team
        else:
            return

    def isProtectionZoneActive(self, zoneID):
        zone = self.getProtectionZoneById(zoneID)
        if zone is not None:
            return zone.isActive
        else:
            return False

    def playerInProtectedZone(self, zoneID, hasPlayerEntered):
        self.__isPlayerInZone[zoneID] = hasPlayerEntered
        self.onPlayerInProtectedZoneAction(zoneID, hasPlayerEntered)

    def isPlayerInProtectedZone(self, zoneID=None):
        if zoneID is None:
            return any(self.__isPlayerInZone.values())
        else:
            if zoneID in self.__isPlayerInZone:
                return self.__isPlayerInZone[zoneID]
            return False