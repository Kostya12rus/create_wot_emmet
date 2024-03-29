# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/game_mode_emulator.py
import sys, BigWorld
from SpaceVisibilityFlags import SpaceVisibilityFlagsFactory
from constants import ARENA_GAMEPLAY_IDS
DEFAULT_VISIBILITY_MASK = -1

def gameModeVisibilityMask(spaceName):
    if 'gameMode' not in sys.argv:
        return DEFAULT_VISIBILITY_MASK
    gameModeArgIndex = sys.argv.index('gameMode') + 1
    if gameModeArgIndex >= len(sys.argv):
        return DEFAULT_VISIBILITY_MASK
    gameMode = sys.argv[gameModeArgIndex].lower()
    if gameMode not in ARENA_GAMEPLAY_IDS:
        return DEFAULT_VISIBILITY_MASK
    spaceVisibilityFlags = SpaceVisibilityFlagsFactory.create(spaceName)
    return spaceVisibilityFlags.getMaskForGameplayID(gameMode)


def createFakeAvatar():
    entityID = BigWorld.createEntity('OfflineEntity', BigWorld.camera().spaceID, 0, (0,
                                                                                     0,
                                                                                     0), (0,
                                                                                          0,
                                                                                          0), {})
    entity = BigWorld.entity(entityID)
    BigWorld.player = lambda : entity