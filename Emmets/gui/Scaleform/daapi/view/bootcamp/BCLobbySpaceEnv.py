# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCLobbySpaceEnv.py
from gui.sounds.ambients import SoundEnv
from gui.sounds.ambients import NoMusic
from gui.sounds.ambients import NoAmbient

class BCLobbySpaceEnv(SoundEnv):

    def __init__(self, soundsCtrl):
        super(BCLobbySpaceEnv, self).__init__(soundsCtrl, 'lobby', music=NoMusic(), ambient=NoAmbient())