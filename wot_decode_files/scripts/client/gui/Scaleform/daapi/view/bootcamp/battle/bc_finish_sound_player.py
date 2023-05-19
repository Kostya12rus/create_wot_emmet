# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/battle/bc_finish_sound_player.py
import SoundGroups
from PlayerEvents import g_playerEvents
from gui.Scaleform.daapi.view.battle.shared.finish_sound_player import FinishSoundPlayer
from gui.battle_control.view_components import IViewComponentsCtrlListener
_SOUND_EVENT_OVERRIDES = {'end_battle_last_kill': 'bc_end_battle_last_kill', 
   'end_battle_capture_base': 'bc_end_battle_capture_base', 
   'time_over': 'bc_end_battle_time_over'}

class BCFinishSoundPlayer(FinishSoundPlayer, IViewComponentsCtrlListener):

    def __init__(self):
        super(BCFinishSoundPlayer, self).__init__()
        self.__soundID = None
        g_playerEvents.onRoundFinished += self.__onRoundFinished
        return

    def detachedFromCtrl(self, ctrlID):
        g_playerEvents.onRoundFinished -= self.__onRoundFinished

    def _playSound(self, soundID):
        self.__soundID = _SOUND_EVENT_OVERRIDES.get(soundID, soundID)

    def __onRoundFinished(self, winnerTeam, reason, extraData):
        if self.__soundID:
            SoundGroups.g_instance.playSound2D(self.__soundID)