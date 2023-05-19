# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/keys_handlers.py
import CommandMapping
from helpers.dependency import replace_none_kwargs
from skeletons.gui.battle_session import IBattleSessionProvider

@replace_none_kwargs(guiSessionProvider=IBattleSessionProvider)
def processAmmoSelection(key, guiSessionProvider=None):
    if CommandMapping.g_instance.isFiredList(xrange(CommandMapping.CMD_AMMO_CHOICE_1, CommandMapping.CMD_AMMO_CHOICE_4), key):
        ammoCtrl = guiSessionProvider.shared.ammo
        if ammoCtrl:
            ammoCtrl.handleAmmoChoice(key)
        return True