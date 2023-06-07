# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/lock_overlays.py
from helpers import dependency
from skeletons.gui.impl import INotificationWindowController

@dependency.replace_none_kwargs(notificationManager=INotificationWindowController)
def lockNotificationManager(lock, source=__name__, releasePostponed=False, fireReleased=True, postponeActive=False, notificationManager=None):
    isLocked = notificationManager.hasLock(source)
    if lock and not isLocked:
        notificationManager.lock(source)
        if postponeActive:
            notificationManager.postponeActive()
    elif not lock and isLocked:
        notificationManager.unlock(source)
        if releasePostponed:
            notificationManager.releasePostponed(fireReleased)