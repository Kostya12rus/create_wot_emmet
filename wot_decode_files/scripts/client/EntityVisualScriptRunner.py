# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/EntityVisualScriptRunner.py
import cPickle, zlib, BigWorld
from script_component.DynamicScriptComponent import DynamicScriptComponent
from visual_script_client.contexts.vehicle_context import VehicleContextClient
from visual_script_client.contexts.entity_context import EntityContextClient

class EntityVisualScriptRunner(DynamicScriptComponent):

    def __init__(self):
        super(EntityVisualScriptRunner, self).__init__()
        self._vsePlans = None
        self._ctx = None
        return

    def _onAvatarReady(self):
        if self.clientPlan:
            player = BigWorld.player()
            arenaInfo = player.arena.arenaInfo
            self._vsePlans = vsePlans = arenaInfo.visualScriptCache.getPlan(self.keyName, [self.clientPlan])
            if self.entity.__class__.__name__ == 'Vehicle':
                self._ctx = VehicleContextClient(self.entity)
            else:
                self._ctx = EntityContextClient(self)
            clientPlanParams = cPickle.loads(zlib.decompress(self.clientPlanParams))
            vsePlans.setContext(self._ctx)
            vsePlans.setOptionalInputParams(**clientPlanParams)
            vsePlans.start()

    def onDestroy(self):
        if self._vsePlans is not None:
            self._vsePlans.stop()
        if self._ctx is not None:
            self._ctx.destroy()
        self._vsePlans = None
        self._ctx = None
        super(EntityVisualScriptRunner, self).onDestroy()
        return