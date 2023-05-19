# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/currency_reserves/sounds.py
from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class SOUNDS(CONST_CONTAINER):
    STATE = 'STATE_overlay_hangar_general'
    ENTER = 'STATE_overlay_hangar_general_on'
    EXIT = 'STATE_overlay_hangar_general_off'


RESERVES_AWARD_SOUND_SPACE = CommonSoundSpaceSettings(name='reserves_award_view', entranceStates={SOUNDS.STATE: SOUNDS.ENTER}, exitStates={SOUNDS.STATE: SOUNDS.EXIT}, enterEvent='', persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True)