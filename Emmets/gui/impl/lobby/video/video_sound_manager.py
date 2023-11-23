# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/video/video_sound_manager.py
from shared_utils import CONST_CONTAINER

class IVideoSoundManager(object):

    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

    def pause(self):
        raise NotImplementedError

    def unpause(self):
        raise NotImplementedError


class DummySoundManager(object):

    def start(self):
        pass

    def stop(self):
        pass

    def pause(self):
        pass

    def unpause(self):
        pass


class SoundManagerStates(CONST_CONTAINER):
    PLAYING = 'playing'
    PAUSE = 'pause'
    STOPPED = 'stopped'