# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/collection/sounds.py
from enum import Enum
from sound_gui_manager import CommonSoundSpaceSettings

class Sounds(Enum):
    SPACE = 'collections_space'
    COMMON_ENTER = 'achievements_enter'
    COMMON_EXIT = 'achievements_exit'
    STATE_PLACE = 'STATE_hangar_place'
    STATE_PLACE_ACHIEVEMENTS = 'STATE_hangar_place_achievements'
    STATE_PLACE_TASKS = 'STATE_hangar_place_tasks'
    REWARD_SCREEN = 'bp_reward_screen'
    MT_BIRTHDAY23_ENTER = 'collections_anniversary13_enter'
    MT_BIRTHDAY23_EXIT = 'collections_anniversary13_exit'


COLLECTIONS_SOUND_SPACE = CommonSoundSpaceSettings(name=Sounds.SPACE.value, entranceStates={Sounds.STATE_PLACE.value: Sounds.STATE_PLACE_ACHIEVEMENTS.value}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=Sounds.COMMON_ENTER.value, exitEvent=Sounds.COMMON_EXIT.value)
COLLECTIONS_MT_BIRTHDAY23_SOUND_SPACE = CommonSoundSpaceSettings(name=Sounds.SPACE.value, entranceStates={}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=Sounds.MT_BIRTHDAY23_ENTER.value, exitEvent=Sounds.MT_BIRTHDAY23_EXIT.value)