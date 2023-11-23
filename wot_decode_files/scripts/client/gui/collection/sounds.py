# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/collection/sounds.py
from enum import Enum
from sound_gui_manager import CommonSoundSpaceSettings

class Sounds(Enum):
    SPACE = 'collections_space'
    STATE_PLACE = 'STATE_hangar_place'
    STATE_PLACE_GARAGE = 'STATE_hangar_place_garage'
    STATE_PLACE_TASKS = 'STATE_hangar_place_tasks'
    REWARD_SCREEN = 'bp_reward_screen'
    MT_BIRTHDAY23_ENTER = 'collections_anniversary13_enter'
    MT_BIRTHDAY23_EXIT = 'collections_anniversary13_exit'


COLLECTIONS_MT_BIRTHDAY23_SOUND_SPACE = CommonSoundSpaceSettings(name=Sounds.SPACE.value, entranceStates={}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=Sounds.MT_BIRTHDAY23_ENTER.value, exitEvent=Sounds.MT_BIRTHDAY23_EXIT.value)