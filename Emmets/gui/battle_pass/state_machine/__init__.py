# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_pass/state_machine/__init__.py
from gui.shared.lock_overlays import lockNotificationManager as doLock
_LOCK_SOURCE_NAME = 'BATTLE_PASS_REWARD_LOGIC'

def lockNotificationManager(lock, notificationManager=None):
    doLock(lock, source=_LOCK_SOURCE_NAME, notificationManager=notificationManager)