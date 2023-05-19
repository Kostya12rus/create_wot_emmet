# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/AimSound.py
import SoundGroups

class AimSound(object):
    TARGET_UNLOCKED = 0
    TARGET_LOCKED = 1
    TARGET_LOST = 2
    aimSounds = (
     ('ui_target_unlocked', 'target_unlocked'),
     ('ui_target_locked', 'target_captured'),
     ('ui_target_lost', 'target_lost'))

    @staticmethod
    def play(state, playerNotifications=None):
        sounds = AimSound.aimSounds[state]
        SoundGroups.g_instance.playSound2D(sounds[0])
        if playerNotifications is not None:
            playerNotifications.play(sounds[1])
        return