# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/mapbox/sound.py
from enum import Enum
from sound_gui_manager import CommonSoundSpaceSettings
import WWISE

class Sounds(Enum):
    OVERLAY_HANGAR_GENERAL = 'STATE_overlay_hangar_general'
    OVERLAY_HANGAR_GENERAL_ON = 'STATE_overlay_hangar_general_on'
    OVERLAY_HANGAR_GENERAL_OFF = 'STATE_overlay_hangar_general_off'


class MapBoxSounds(Enum):
    REWARD_SCREEN = 'bp_reward_screen'


def getMapboxViewSoundSpace(enterEvent='', exitEvent=''):
    return CommonSoundSpaceSettings(name='mapbox_view', entranceStates={Sounds.OVERLAY_HANGAR_GENERAL.value: Sounds.OVERLAY_HANGAR_GENERAL_ON.value}, exitStates={Sounds.OVERLAY_HANGAR_GENERAL.value: Sounds.OVERLAY_HANGAR_GENERAL_OFF.value}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=enterEvent, exitEvent=exitEvent)


def playSound(eventName):
    WWISE.WW_eventGlobal(eventName)