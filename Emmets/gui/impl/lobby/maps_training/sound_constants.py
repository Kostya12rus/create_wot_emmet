# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/maps_training/sound_constants.py
import WWISE
from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER

class MapsTrainingSound(CONST_CONTAINER):
    COMMON_SOUND_SPACE = 'Lobby_music_garage_maps_training'
    GAMEMODE_GROUP = 'STATE_gamemode'
    GAMEMODE_STATE = 'STATE_gamemode_maps_training'
    GAMEMODE_DEFAULT = 'STATE_gamemode_default'
    HANGAR_GROUP = 'STATE_hangar_place'
    HANGAR_STATE = 'STATE_hangar_place_garage'
    ENTER_EVENT = 'mt_mode_enter'
    EXIT_EVENT = 'mt_mode_exit'
    MAP_CHOICE_ENTER = 'mt_map_choice_enter'
    MAP_CHOICE_EXIT = 'mt_map_choice_exit'
    COMPLETE_ITEM = 'mt_anim_scenario_complete'

    @staticmethod
    def onSelectedMap(isSelected):
        if isSelected:
            WWISE.WW_eventGlobal(MapsTrainingSound.MAP_CHOICE_EXIT)
        else:
            WWISE.WW_eventGlobal(MapsTrainingSound.MAP_CHOICE_ENTER)


MAPS_TRAINING_SOUND_SPACE = CommonSoundSpaceSettings(name=MapsTrainingSound.COMMON_SOUND_SPACE, entranceStates={MapsTrainingSound.GAMEMODE_GROUP: MapsTrainingSound.GAMEMODE_STATE, MapsTrainingSound.HANGAR_GROUP: MapsTrainingSound.HANGAR_STATE}, exitStates={MapsTrainingSound.GAMEMODE_GROUP: MapsTrainingSound.GAMEMODE_DEFAULT}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=MapsTrainingSound.ENTER_EVENT, exitEvent=MapsTrainingSound.EXIT_EVENT)