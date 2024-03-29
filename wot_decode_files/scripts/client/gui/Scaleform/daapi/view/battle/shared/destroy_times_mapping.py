# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/destroy_times_mapping.py
import SoundGroups
from constants import VEHICLE_MISC_STATUS, DEATH_ZONES
from debug_utils import LOG_ERROR
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_TYPES import BATTLE_NOTIFICATIONS_TIMER_TYPES
_TIMER_STATES = BATTLE_NOTIFICATIONS_TIMER_TYPES

def getDefaultMiscStatuses():
    return {VEHICLE_MISC_STATUS.VEHICLE_DROWN_WARNING: _TIMER_STATES.DROWN, 
       VEHICLE_MISC_STATUS.VEHICLE_IS_OVERTURNED: _TIMER_STATES.OVERTURNED}


def getDefaultDeathZonesCodes():
    return {DEATH_ZONES.STATIC: _TIMER_STATES.DEATH_ZONE}


def getDefaultDeathZonesTexts():
    return {DEATH_ZONES.STATIC: ''}


def getTimerViewTypeID(level):
    if level == 'critical':
        typeID = _TIMER_STATES.CRITICAL_VIEW
    elif level == 'warning':
        typeID = _TIMER_STATES.WARNING_VIEW
    else:
        LOG_ERROR('Type of view is not found by level', level)
        typeID = _TIMER_STATES.WARNING_VIEW
    return typeID


class FrontendMapping(object):
    __slots__ = ('__miscStatuses', '__deathZonesCodes', '__deathZonesSounds')

    def __init__(self, miscStatuses=None, deathZonesCodes=None, deathZonesSoundIDs=None, deathZonesTexts=None):
        super(FrontendMapping, self).__init__()
        self.__miscStatuses = miscStatuses or getDefaultMiscStatuses()
        self.__deathZonesCodes = deathZonesCodes or getDefaultDeathZonesCodes()
        self.__deathZonesSounds = self.__loadDeathZoneSounds(deathZonesSoundIDs or {})

    def clear(self):
        self.__miscStatuses.clear()
        self.__deathZonesCodes.clear()
        self.__deathZonesSounds.clear()

    def getTimerTypeIDByMiscCode(self, code):
        if code in self.__miscStatuses:
            return self.__miscStatuses[code]
        else:
            LOG_ERROR('Destroy timer is not found by code', code)
            return

    def getTimerTypeIDByDeathZoneCode(self, code):
        if code in self.__deathZonesCodes:
            return self.__deathZonesCodes[code]
        else:
            LOG_ERROR('Death zone timer is not found by code', code)
            return

    def getDestroyTimersTypesIDs(self):
        return self.__miscStatuses.values()

    def getDeathZoneTimersTypesIDs(self):
        return self.__deathZonesCodes.values()

    def getSoundByDeathZone(self, code, level):
        sound = None
        key = (code, level)
        if key in self.__deathZonesSounds:
            sound = self.__deathZonesSounds[code]
        return sound

    @staticmethod
    def __loadDeathZoneSounds(soundsIDs):
        sounds = {}
        for key, soundID in soundsIDs.iteritems():
            sounds[key] = SoundGroups.g_instance.getSound2D(soundID)

        return sounds