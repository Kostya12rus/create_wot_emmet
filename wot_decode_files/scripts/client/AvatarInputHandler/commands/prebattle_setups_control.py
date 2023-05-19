# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/commands/prebattle_setups_control.py
import CommandMapping
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand
from gui.battle_control import event_dispatcher
_SETUP_CMDS = (
 CommandMapping.CMD_AMMUNITION_SHORTCUT_SWITCH_SETUP_1,
 CommandMapping.CMD_AMMUNITION_SHORTCUT_SWITCH_SETUP_2)

class PrebattleSetupsControl(InputHandlerCommand):

    def handleKeyEvent(self, isDown, key, mods, event=None):
        if CommandMapping.g_instance.isFiredList(_SETUP_CMDS, key) and isDown:
            event_dispatcher.changeAmmunitionSetup(key)
            return True
        return False