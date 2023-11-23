# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/VehicleRespawnComponent.py
import Event
from script_component.DynamicScriptComponent import DynamicScriptComponent

class VehicleRespawnComponent(DynamicScriptComponent):
    onSetSpawnTime = Event.Event()

    def chooseSpawnGroup(self, groupName):
        self.cell.chooseSpawnGroup(groupName)

    def set_spawnTime(self, prev):
        self.onSetSpawnTime(self.entity.id, self.spawnTime)