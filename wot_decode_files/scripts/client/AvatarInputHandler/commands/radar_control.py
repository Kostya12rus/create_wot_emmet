# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/commands/radar_control.py
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
import CommandMapping

class RadarControl(InputHandlerCommand):
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def handleKeyEvent(self, isDown, key, mods, event=None):
        if self.__guiSessionProvider.dynamic.radar:
            if isDown and CommandMapping.g_instance.isFired(CommandMapping.CMD_CM_VEHICLE_ACTIVATE_RADAR, key):
                self.__guiSessionProvider.dynamic.radar.activateRadar()
                return True
        return False