# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/comp7/comp7_lobby_sounds.py
from enum import Enum
import SoundGroups
from gui.impl.gen.view_models.views.lobby.comp7.meta_view.root_view_model import MetaRootViews
from sound_gui_manager import CommonSoundSpaceSettings

class MetaViewSounds(Enum):
    ENTER_EVENT = 'comp_7_progression_enter'
    EXIT_EVENT = 'comp_7_progression_exit'
    ENTER_TAB_EVENTS = {MetaRootViews.RANKREWARDS: 'comp_7_rank_rewards_enter', 
       MetaRootViews.YEARLYSTATISTICS: 'comp_7_season_statistics_screen_appear'}


def getComp7MetaSoundSpace():
    return CommonSoundSpaceSettings(name='comp7_meta_view', entranceStates={}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=MetaViewSounds.ENTER_EVENT.value, exitEvent=MetaViewSounds.EXIT_EVENT.value)


def playComp7MetaViewTabSound(tabId):
    soundName = MetaViewSounds.ENTER_TAB_EVENTS.value.get(tabId)
    if soundName is not None:
        SoundGroups.g_instance.playSound2D(soundName)
    return