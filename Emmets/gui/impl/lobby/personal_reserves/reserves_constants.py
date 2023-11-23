# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/personal_reserves/reserves_constants.py
from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class SOUNDS(CONST_CONTAINER):
    COMMON_SOUND_SPACE = 'personalReserves'
    STATE_PLACE = 'STATE_hangar_place'
    STATE_PLACE_PERSONAL_RESERVES = 'STATE_hangar_place_personal_reserves'
    STATE_PLACE_HANGAR = 'STATE_hangar_place_garage'
    ENTER_EVENT = 'personal_reserves'


PERSONAL_RESERVES_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.COMMON_SOUND_SPACE, entranceStates={SOUNDS.STATE_PLACE: SOUNDS.STATE_PLACE_PERSONAL_RESERVES}, exitStates={SOUNDS.STATE_PLACE: SOUNDS.STATE_PLACE_HANGAR}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=SOUNDS.ENTER_EVENT, exitEvent='')