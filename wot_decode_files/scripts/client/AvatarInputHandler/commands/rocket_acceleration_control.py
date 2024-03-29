# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/commands/rocket_acceleration_control.py
import BigWorld, CommandMapping
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand

class RocketAccelerationControl(InputHandlerCommand):

    def handleKeyEvent(self, isDown, key, mods, event=None):
        cmdMap = CommandMapping.g_instance
        keyCaptured = cmdMap.isFired(CommandMapping.CMD_CM_VEHICLE_SWITCH_AUTOROTATION, key) and isDown
        if not keyCaptured:
            return False
        else:
            vehicle = BigWorld.player().getVehicleAttached()
            if vehicle is not None and vehicle.isPlayerVehicle and vehicle.isAlive():
                self.__activateRocketAcceleration(vehicle)
            return True

    def __activateRocketAcceleration(self, vehicle):
        comp = vehicle.dynamicComponents.get('rocketAccelerationController', None)
        if comp is not None:
            comp.tryActivate()
        return