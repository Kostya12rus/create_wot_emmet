# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_pass/state_machine/__init__.py
from helpers import dependency
from skeletons.gui.impl import INotificationWindowController
_LOCK_SOURCE_NAME = 'BATTLE_PASS_REWARD_LOGIC'

@dependency.replace_none_kwargs(notificationManager=INotificationWindowController)
def lockNotificationManager(lock, notificationManager=None):
    isLocked = notificationManager.hasLock(_LOCK_SOURCE_NAME)
    if lock and not isLocked:
        notificationManager.lock(_LOCK_SOURCE_NAME)
    elif not lock and isLocked:
        notificationManager.unlock(_LOCK_SOURCE_NAME)