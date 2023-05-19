# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/mode_selector/sound_constants.py
from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER

class ModeSelectorSound(CONST_CONTAINER):
    COMMON_SOUND_SPACE = 'mode_selector'
    STATE_PLACE = 'STATE_mode_selector'
    STATE_MODE_SELECTOR_ON = 'STATE_mode_selector_on'
    STATE_MODE_SELECTOR_OFF = 'STATE_mode_selector_off'
    ENTER_EVENT = 'ev_mode_selector_enter'
    EXIT_EVENT = 'ev_mode_selector_exit'


MODE_SELECTOR_SOUND_SPACE = CommonSoundSpaceSettings(name=ModeSelectorSound.COMMON_SOUND_SPACE, entranceStates={ModeSelectorSound.STATE_PLACE: ModeSelectorSound.STATE_MODE_SELECTOR_ON}, exitStates={ModeSelectorSound.STATE_PLACE: ModeSelectorSound.STATE_MODE_SELECTOR_OFF}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=ModeSelectorSound.ENTER_EVENT, exitEvent=ModeSelectorSound.EXIT_EVENT)