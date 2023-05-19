# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/store/browser/sound_constants.py
from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER

class SOUNDS(CONST_CONTAINER):
    COMMON_SOUND_SPACE = 'shop'
    VEHICLE_PREVIEW_SOUND_SPACE = 'shopVehiclePreview'
    STATE_PLACE = 'STATE_hangar_place'
    STATE_PLACE_SHOP = 'STATE_hangar_place_shop'
    STATE_PLACE_VEHICLE_PREVIEW = 'STATE_hangar_place_shop_preview'
    ENTER = 'shop_enter'
    EXIT = 'shop_exit'


SHOP_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.COMMON_SOUND_SPACE, entranceStates={SOUNDS.STATE_PLACE: SOUNDS.STATE_PLACE_SHOP}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=SOUNDS.ENTER, exitEvent=SOUNDS.EXIT)
SHOP_PREVIEW_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.VEHICLE_PREVIEW_SOUND_SPACE, entranceStates={SOUNDS.STATE_PLACE: SOUNDS.STATE_PLACE_VEHICLE_PREVIEW}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent='', exitEvent='', parentSpace=SOUNDS.COMMON_SOUND_SPACE)