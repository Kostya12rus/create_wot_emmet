# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/death_zones_mapping.py
import ArenaType
from Math import Vector2
import Math
ZONES_X = 10
ZONES_Y = 10
DEATH_ZONE_IDS = range(0, ZONES_X * ZONES_Y)

def getZoneIdFromPosition(arenaTypeID, position):
    return Math.getZoneIdFromPosition(*(ArenaType.g_cache[arenaTypeID].boundingBox + (position,)))


def getZoneBoundsFromId(arenaTypeID, zoneId):
    lowerLeft, upperRight = ArenaType.g_cache[arenaTypeID].boundingBox
    lowerLeft = Vector2(*lowerLeft)
    upperRight = Vector2(*upperRight)
    x = zoneId % ZONES_X
    y = zoneId / ZONES_X
    stepX, stepY = (upperRight - lowerLeft).tuple()
    stepX = stepX / ZONES_X
    stepY = stepY / ZONES_Y
    return (lowerLeft + Vector2(x * stepX, y * stepY), lowerLeft + Vector2((x + 1) * stepX, (y + 1) * stepY))


def getZoneCenterFromId(arenaTypeID, zoneId):
    lowerLeft, upperRight = getZoneBoundsFromId(arenaTypeID, zoneId)
    return lowerLeft + (upperRight - lowerLeft) / 2.0