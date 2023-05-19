# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/sounds/sound_systems/__init__.py
import WWISE
from gui.sounds.sound_systems import wwise_system, no_system
__all__ = ('getCurrentSoundSystem', )

def getCurrentSoundSystem():
    if WWISE.enabled:
        return wwise_system.WWISESoundSystem()
    return no_system.NoSoundSystem()