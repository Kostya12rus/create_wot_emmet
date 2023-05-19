# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/avatar_components/vehicle_removal_controller.py
import BigWorld
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from helpers import uniprof

class VehicleRemovalController(object):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def onBecomePlayer(self):
        pass

    def handleKey(self, isDown, key, mods):
        pass

    def onBecomeNonPlayer(self):
        pass

    @uniprof.regionDecorator(label='VehicleRemovalController.removeVehicle', scope='wrap')
    def removeVehicle(self, vehID):
        vehicle = BigWorld.entity(vehID)
        if vehicle is None:
            return
        else:
            vehicle.show(False)
            return