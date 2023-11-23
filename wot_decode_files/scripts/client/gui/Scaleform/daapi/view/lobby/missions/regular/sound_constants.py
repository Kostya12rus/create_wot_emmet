# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/missions/regular/sound_constants.py
from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER

class SOUNDS(CONST_CONTAINER):
    COMMON_SOUND_SPACE = 'tasks'
    STATE_PLACE = 'STATE_hangar_place'
    STATE_PLACE_TASKS = 'STATE_hangar_place_tasks'
    ENTER = 'tasks_bp_s12_enter'
    EXIT = 'tasks_bp_s12_exit'


TASKS_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.COMMON_SOUND_SPACE, entranceStates={SOUNDS.STATE_PLACE: SOUNDS.STATE_PLACE_TASKS}, exitStates={}, enterEvent=SOUNDS.ENTER, exitEvent=SOUNDS.EXIT, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True)