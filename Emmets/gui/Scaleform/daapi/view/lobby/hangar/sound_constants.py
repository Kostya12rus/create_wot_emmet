# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/sound_constants.py
from sound_gui_manager import CommonSoundSpaceSettings
from gui.sounds.filters import States, StatesGroup
FIELD_POST_SOUND_SETTINGS = CommonSoundSpaceSettings(name='field_post', entranceStates={'STATE_hangar_place': 'STATE_hangar_place_garage', 
   StatesGroup.HANGAR_FILTERED: States.HANGAR_FILTERED_ON}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent='', exitEvent='')
BROWSER_VIEW_SOUND_SPACES = {FIELD_POST_SOUND_SETTINGS.name: FIELD_POST_SOUND_SETTINGS}