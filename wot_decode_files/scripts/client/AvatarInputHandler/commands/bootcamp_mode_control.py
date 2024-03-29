# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/commands/bootcamp_mode_control.py
import BigWorld, constants, Keys
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand

class BootcampModeControl(InputHandlerCommand):

    def handleKeyEvent(self, isDown, key, mods, event=None):
        playerBase = BigWorld.player().base
        if isDown and constants.HAS_DEV_RESOURCES:
            if key == Keys.KEY_F3:
                playerBase.setDevelopmentFeature(0, 'heal', 0, '')
                return True
            if key == Keys.KEY_F4:
                playerBase.setDevelopmentFeature(0, 'reload_gun', 0, '')
                return True
            if key == Keys.KEY_F5:
                playerBase.setDevelopmentFeature(0, 'teleportToShotPoint', 0, '')
                return True
            if key == Keys.KEY_P and BigWorld.isKeyDown(Keys.KEY_CAPSLOCK):
                playerBase.setDevelopmentFeature(0, 'kill_bots', 0, '')
                return True