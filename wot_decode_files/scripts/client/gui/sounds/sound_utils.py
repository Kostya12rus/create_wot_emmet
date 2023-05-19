# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/sounds/sound_utils.py
from debug_utils import LOG_DEBUG
from gui.sounds.sound_constants import IS_ADVANCED_LOGGING
if IS_ADVANCED_LOGGING:

    def SOUND_DEBUG(msg, *kargs):
        LOG_DEBUG('[SOUND]', msg, kargs)


else:

    def SOUND_DEBUG(msg, *kargs):
        pass