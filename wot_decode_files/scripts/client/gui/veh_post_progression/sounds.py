# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/veh_post_progression/sounds.py
from shared_utils import CONST_CONTAINER
import WWISE
from sound_gui_manager import CommonSoundSpaceSettings

def playSound(eventName):
    WWISE.WW_eventGlobal(eventName)


class Sounds(CONST_CONTAINER):
    STATE_PLACE = 'STATE_hangar_place'
    STATE_PLACE_PP = 'STATE_hangar_place_post_progression'
    COMMON_SOUND_SPACE = 'post_progression_space'
    ENTER = 'ev_pp_enter'
    ENTER_ELITE_VIEW = 'ev_pp_elite_status_acquired'
    MODIFICATION_DESTROY = 'ev_pp_modification_destroy'
    MODIFICATION_MOUNT = 'ev_pp_modification_mount'
    SETUP_SWITCH = 'ev_pp_setup_switch'
    GAMEPLAY_SETUP_SWITCH = 'ev_pp_gameplay_setup_switch'


PP_VIEW_SOUND_SPACE = CommonSoundSpaceSettings(name=Sounds.COMMON_SOUND_SPACE, entranceStates={Sounds.STATE_PLACE: Sounds.STATE_PLACE_PP}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=Sounds.ENTER, exitEvent='')