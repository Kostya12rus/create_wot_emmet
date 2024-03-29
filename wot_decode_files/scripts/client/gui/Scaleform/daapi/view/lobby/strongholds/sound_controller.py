# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/strongholds/sound_controller.py
from gui.app_loader import sf_lobby
from gui.shared.SoundEffectsId import SoundEffectsId

class _StrongholdSoundController(object):

    @sf_lobby
    def app(self):
        return

    def init(self):
        pass

    def fini(self):
        pass

    def playBattleRoomTimerAlert(self):
        self.__playSound(SoundEffectsId.BATTLE_ROOM_TIMER_ALERT)

    def __playSound(self, soundID):
        app = self.app
        if app is not None and app.soundManager is not None:
            app.soundManager.playEffectSound(soundID)
        return


g_strongholdSoundController = _StrongholdSoundController()