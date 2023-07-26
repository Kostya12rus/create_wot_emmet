# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/common/sound_constants.py
from sound_gui_manager import CommonSoundSpaceSettings
from gui.sounds.filters import States, StatesGroup
FIELD_POST_SOUND_SETTINGS = CommonSoundSpaceSettings(name='field_post', entranceStates={'STATE_hangar_place': 'STATE_hangar_place_garage', 
   StatesGroup.HANGAR_FILTERED: States.HANGAR_FILTERED_ON}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent='', exitEvent='')
SUBVIEW_SOUND_SPACE = CommonSoundSpaceSettings(name='sub_view', entranceStates={'STATE_hangar_place': 'STATE_hangar_place_garage', 
   StatesGroup.HANGAR_FILTERED: States.HANGAR_FILTERED_ON}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent='', exitEvent='')
BROWSER_VIEW_SOUND_SPACES = {FIELD_POST_SOUND_SETTINGS.name: FIELD_POST_SOUND_SETTINGS, 
   SUBVIEW_SOUND_SPACE.name: SUBVIEW_SOUND_SPACE}