# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/items/writers/sound_writers.py
import math, ResMgr
from items import _xml
from items.components import sound_components
from items.writers import shared_writers

def writeWWTripleSoundConfig(soundConfig, section):
    _xml.rewriteString(section, 'wwsound', soundConfig.wwsound, defaultValue='')
    _xml.rewriteString(section, 'wwsoundPC', soundConfig.wwsoundPC, defaultValue='')
    _xml.rewriteString(section, 'wwsoundNPC', soundConfig.wwsoundNPC, defaultValue='')


def writeHullAimingSound(hullAimingSound, section, cache):
    if hullAimingSound is None:
        return _xml.deleteAndCleanup(section, 'hullAiming/audio')
    else:
        changed = False
        audioKey = 'hullAiming/audio/'
        changed |= shared_writers.writeLodDist(hullAimingSound.lodDist, section, audioKey + 'lodDist', cache)
        changed |= _xml.rewriteFloat(section, audioKey + 'angleLimitValue', math.degrees(hullAimingSound.angleLimitValue))
        soundsKey = audioKey + 'sounds/'
        soundsDS = _xml.ListRewriter(section, soundsKey + '*')
        for sound in hullAimingSound.sounds:
            soundDS = soundsDS.next(preferredPredicate=lambda ds, snd=sound: ds.name == snd.state, path=soundsKey + sound.state)
            changed |= _xml.rewriteString(soundDS, 'underLimitSounds/wwsoundPC', sound.underLimitSounds.PC)
            changed |= _xml.rewriteString(soundDS, 'underLimitSounds/wwsoundNPC', sound.underLimitSounds.NPC)
            changed |= _xml.rewriteString(soundDS, 'overLimitSounds/wwsoundPC', sound.overLimitSounds.PC)
            changed |= _xml.rewriteString(soundDS, 'overLimitSounds/wwsoundNPC', sound.overLimitSounds.NPC)

        changed |= soundsDS.flush()
        return changed