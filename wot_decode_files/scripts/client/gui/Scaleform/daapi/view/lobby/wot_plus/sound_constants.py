# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/wot_plus/sound_constants.py
from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class SOUNDS(CONST_CONTAINER):
    INFO_PAGE_NAME = 'wot_plus_info_page'
    VEHICLE_RENTAL_PAGE_NAME = 'vehicle_rental_page'
    OVERLAY_HANGAR_GENERAL = 'STATE_overlay_hangar_general'
    OVERLAY_HANGAR_GENERAL_ON = 'STATE_overlay_hangar_general_on'
    OVERLAY_HANGAR_GENERAL_OFF = 'STATE_overlay_hangar_general_off'


WOT_PLUS_INFO_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.INFO_PAGE_NAME, entranceStates={SOUNDS.OVERLAY_HANGAR_GENERAL: SOUNDS.OVERLAY_HANGAR_GENERAL_ON}, exitStates={SOUNDS.OVERLAY_HANGAR_GENERAL: SOUNDS.OVERLAY_HANGAR_GENERAL_OFF}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent='', exitEvent='')
VEHICLE_RENTAL_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.VEHICLE_RENTAL_PAGE_NAME, entranceStates={SOUNDS.OVERLAY_HANGAR_GENERAL: SOUNDS.OVERLAY_HANGAR_GENERAL_ON}, exitStates={SOUNDS.OVERLAY_HANGAR_GENERAL: SOUNDS.OVERLAY_HANGAR_GENERAL_OFF}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent='', exitEvent='')