# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/sounds/abstract.py
from gui.sounds.sound_constants import SoundSystems, SPEAKERS_CONFIG

class SoundSystemAbstract(object):

    def getID(self):
        raise NotImplementedError

    def init(self):
        pass

    def fini(self):
        pass

    def isMSR(self):
        return False

    def enableDynamicPreset(self):
        pass

    def disableDynamicPreset(self):
        pass

    def setSoundSystem(self, value):
        pass

    def setBassBoost(self, isEnabled):
        pass

    def getSystemSpeakersPresetID(self):
        return SPEAKERS_CONFIG.AUTO_DETECTION

    def getUserSpeakersPresetID(self):
        return SPEAKERS_CONFIG.AUTO_DETECTION

    def setUserSpeakersPresetID(self, presetID):
        pass

    def sendGlobalEvent(self, eventName, **params):
        pass

    def onEnvStart(self, environment):
        pass

    def onEnvStop(self, environment):
        pass

    def __repr__(self):
        return 'SoundSystem(%s)' % SoundSystems.getUserName(self.getID())