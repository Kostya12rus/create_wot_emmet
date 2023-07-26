# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/commands/auto_shoot_gun_control.py
import BigWorld, CommandMapping
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class AutoShootGunControl(InputHandlerCommand):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def handleKeyEvent(self, isDown, key, mods, event=None):
        if not (CommandMapping.g_instance.isFired(CommandMapping.CMD_CM_SHOOT, key) and isDown):
            return False
        else:
            vehicle = BigWorld.player().getVehicleAttached()
            if vehicle is None or not vehicle.isPlayerVehicle or not vehicle.isAlive():
                return False
            autoShootGunCtrl = self.__sessionProvider.shared.autoShootGunCtrl
            if autoShootGunCtrl is None:
                return False
            autoShootGunCtrl.burstController.processShootCmd()
            return True